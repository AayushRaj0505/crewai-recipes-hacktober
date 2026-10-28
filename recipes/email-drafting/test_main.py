"""Smoke test for email-drafting recipe main execution with mocked LLM."""

import os
from unittest.mock import patch

from crewai import Crew, Process

os.environ["LLM_API_KEY"] = "nvapi-test"

from crew import build_crew  # noqa: E402


def test_crew_build_and_kickoff() -> None:
    """Verify build_crew instantiates Crew and kickoff runs smoothly."""
    crew = build_crew(
        recipient="Team",
        purpose="Status update",
        key_points="Project on track",
        tone="professional",
    )
    assert len(crew.agents) == 2
    assert len(crew.tasks) == 2

    with patch("crewai.Crew.kickoff", return_value="Mocked Polished Email"):
        result = crew.kickoff()
        assert result == "Mocked Polished Email"


def test_crew_structure_and_process() -> None:
    """Verify the crew contains the expected agents and tasks and runs sequentially."""
    crew = build_crew(
        recipient="Test Recipient",
        purpose="Test Purpose",
        key_points="Test Key Point",
        tone="test-tone",
    )

    assert isinstance(crew, Crew)
    assert len(crew.agents) == 2
    assert len(crew.tasks) == 2
    assert crew.process == Process.sequential


def test_editing_task_uses_drafting_task_as_context() -> None:
    """Verify the editing task receives the drafting task as context."""
    crew = build_crew(
        recipient="Test Recipient",
        purpose="Test Purpose",
        key_points="Test Key Point",
        tone="test-tone",
    )

    drafting_task, editing_task = crew.tasks
    assert drafting_task in editing_task.context


def test_task_descriptions_interpolate_inputs() -> None:
    """Verify supplied brief values appear in the task descriptions."""
    values = {
        "recipient": "Recipient For Test",
        "purpose": "Purpose For Test",
        "key_points": "Key Point For Test",
        "tone": "Tone For Test",
    }
    crew = build_crew(**values)
    descriptions = " ".join(task.description for task in crew.tasks)

    for value in values.values():
        assert value in descriptions


def test_agents_do_not_delegate() -> None:
    """Verify delegation is disabled for every constructed agent."""
    crew = build_crew(
        recipient="Test Recipient",
        purpose="Test Purpose",
        key_points="Test Key Point",
        tone="test-tone",
    )

    assert all(agent.allow_delegation is False for agent in crew.agents)


if __name__ == "__main__":
    test_crew_build_and_kickoff()
    print("✅ email-drafting: test_main passed")
