"""
AI Study Planner Recipe — agents.py

Defines the 3 agents for the study planning crew:
1. Curriculum Planner
2. Study Strategy Planner
3. Study Plan Synthesizer
"""

from crewai import Agent

from llm import get_llm


def build_agents() -> tuple[Agent, Agent, Agent]:
    """Build and return the study planning workflow agents.

    Returns:
        A tuple of (curriculum_planner, strategy_planner, synthesizer).
    """
    llm = get_llm()

    curriculum_planner = Agent(
        role="Curriculum Planner",
        goal=(
            "Deconstruct a learning goal into logical topics, identify essential "
            "prerequisites, and arrange topics progressively from foundational to advanced."
        ),
        backstory=(
            "You are an expert instructional designer and curriculum architect. "
            "You specialize in breaking down complex domains into structured, sequential, "
            "and pedagogically sound learning modules tailored to the learner's starting level."
        ),
        verbose=True,
        memory=False,
        llm=llm,
    )

    strategy_planner = Agent(
        role="Study Strategy Planner",
        goal=(
            "Allocate available study hours across topics, recommend practical exercises "
            "and projects, and design sustainable revision strategies."
        ),
        backstory=(
            "You are a dedicated learning strategist and academic coach with expertise in "
            "cognitive load theory, spaced repetition, and time blocking. You build realistic, "
            "hands-on study schedules that prevent burnout and maximize retention."
        ),
        verbose=True,
        memory=False,
        llm=llm,
    )

    synthesizer = Agent(
        role="Study Plan Synthesizer",
        goal=(
            "Synthesize curriculum modules and study strategies into a unified, concise, "
            "and highly actionable study roadmap with milestones and expected outcomes."
        ),
        backstory=(
            "You are a master technical educator and documentation specialist. You transform "
            "raw curriculum breakdowns and study timetables into clear, engaging, and motivating "
            "step-by-step study plans that learners can execute immediately."
        ),
        verbose=True,
        memory=False,
        llm=llm,
    )

    return curriculum_planner, strategy_planner, synthesizer
