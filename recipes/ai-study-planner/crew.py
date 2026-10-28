"""
AI Study Planner Recipe — crew.py

Assembles the 3-agent study planning workflow Crew:
Curriculum Planner → Study Strategy Planner → Study Plan Synthesizer.
"""

from crewai import Crew, Process

from agents import build_agents
from tasks import build_tasks


def build_crew(
    learning_goal: str,
    available_time: str,
    skill_level: str = "Beginner",
    learning_style: str = "project-based",
) -> Crew:
    """Build and return the AI Study Planner Crew.

    The parameter names match the keys declared in inputs.json:
    - learning_goal
    - available_time
    - skill_level
    - learning_style

    Args:
        learning_goal: What the learner wants to learn (e.g. 'Learn Python for data analysis').
        available_time: Total study time available (e.g. '2 hours per day for 4 weeks').
        skill_level: Starting proficiency level (e.g. 'Beginner').
        learning_style: Preferred learning style (e.g. 'project-based').

    Returns:
        A configured Crew instance ready to call .kickoff().
    """
    curriculum_planner, strategy_planner, synthesizer = build_agents()
    tasks = build_tasks(
        curriculum_planner,
        strategy_planner,
        synthesizer,
        learning_goal=learning_goal,
        available_time=available_time,
        skill_level=skill_level,
        learning_style=learning_style,
    )

    crew = Crew(
        agents=[curriculum_planner, strategy_planner, synthesizer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )
    return crew
