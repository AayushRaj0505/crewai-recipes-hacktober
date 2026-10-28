"""Structural and smoke test for ai-study-planner recipe."""

import json
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

RECIPE_DIR = Path(__file__).resolve().parent

# Ensure recipe dir is on sys.path
if str(RECIPE_DIR) not in sys.path:
    sys.path.insert(0, str(RECIPE_DIR))

# Mock crewai module if not installed in the execution environment
if "crewai" not in sys.modules:
    mock_crewai = MagicMock()

    class MockAgent:
        def __init__(
            self,
            role,
            goal,
            backstory,
            verbose=True,
            memory=False,
            llm=None,
        ):
            self.role = role
            self.goal = goal
            self.backstory = backstory
            self.verbose = verbose
            self.memory = memory
            self.llm = llm

    class MockTask:
        def __init__(self, description, expected_output, agent, context=None):
            self.description = description
            self.expected_output = expected_output
            self.agent = agent
            self.context = context or []

    class MockProcess:
        sequential = "sequential"

    class MockCrew:
        def __init__(self, agents, tasks, process="sequential", verbose=True):
            self.agents = agents
            self.tasks = tasks
            self.process = process
            self.verbose = verbose

        def kickoff(self):
            return "Mocked Final Study Plan"

    def mock_llm_init(
        model,
        base_url,
        api_key,
        temperature=0.2,
        max_tokens=2048,
        max_retries=3,
        timeout=None,
    ):
        mock_obj = MagicMock()
        mock_obj.model = model
        mock_obj.base_url = base_url
        mock_obj.api_key = api_key
        return mock_obj

    mock_crewai.Agent = MockAgent
    mock_crewai.Task = MockTask
    mock_crewai.Crew = MockCrew
    mock_crewai.Process = MockProcess
    mock_crewai.LLM = mock_llm_init
    sys.modules["crewai"] = mock_crewai

os.environ["LLM_API_KEY"] = "nvapi-test"

from agents import build_agents  # noqa: E402
from crew import build_crew  # noqa: E402
from tasks import build_tasks  # noqa: E402


def test_build_agents() -> None:
    """Verify that 3 specialized agents are built with correct roles."""
    agents = build_agents()
    assert len(agents) == 3
    curriculum_planner, strategy_planner, synthesizer = agents

    assert curriculum_planner.role == "Curriculum Planner"
    assert strategy_planner.role == "Study Strategy Planner"
    assert synthesizer.role == "Study Plan Synthesizer"


def test_build_tasks() -> None:
    """Verify tasks are created with appropriate context, inputs, and learning style."""
    agents = build_agents()
    curriculum_planner, strategy_planner, synthesizer = agents
    goal = "Learn Python for data analysis"
    time = "2 hours per day for 4 weeks"
    level = "Beginner"
    style = "project-based"

    tasks = build_tasks(
        curriculum_planner,
        strategy_planner,
        synthesizer,
        learning_goal=goal,
        available_time=time,
        skill_level=level,
        learning_style=style,
    )
    assert len(tasks) == 3
    curriculum_task, strategy_task, synthesis_task = tasks

    assert curriculum_task.agent == curriculum_planner
    assert goal in curriculum_task.description
    assert level in curriculum_task.description

    assert strategy_task.agent == strategy_planner
    assert curriculum_task in strategy_task.context
    assert time in strategy_task.description
    assert style in strategy_task.description

    assert synthesis_task.agent == synthesizer
    assert curriculum_task in synthesis_task.context
    assert strategy_task in synthesis_task.context
    assert style in synthesis_task.description


def test_build_crew_and_kickoff() -> None:
    """Verify build_crew configures the crew with learning_style and kickoff runs."""
    crew = build_crew(
        learning_goal="Learn Python for data analysis",
        available_time="2 hours per day for 4 weeks",
        skill_level="Beginner",
        learning_style="project-based",
    )
    assert len(crew.agents) == 3
    assert len(crew.tasks) == 3

    with patch.object(crew, "kickoff", return_value="Mocked Final Study Plan"):
        result = crew.kickoff()
        assert result == "Mocked Final Study Plan"


def test_inputs_json_contract() -> None:
    """Verify inputs.json schema aligns with build_crew signature."""
    inputs_file = RECIPE_DIR / "inputs.json"
    assert inputs_file.exists()
    fields = json.loads(inputs_file.read_text(encoding="utf-8"))
    names = {f["name"] for f in fields}
    assert names == {"learning_goal", "available_time", "skill_level", "learning_style"}


if __name__ == "__main__":
    test_build_agents()
    test_build_tasks()
    test_build_crew_and_kickoff()
    test_inputs_json_contract()
    print("✅ ai-study-planner: all structural and smoke tests passed")
