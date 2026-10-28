"""
AI Study Planner Recipe — tasks.py

Defines 3 sequential tasks for creating a structured study plan:
1. Curriculum Planning (topics, prerequisites, ordering)
2. Study Strategy (time allocation, practice, revision)
3. Study Plan Synthesis (cohesive, actionable final study plan)
"""

from crewai import Agent, Task


def build_tasks(
    curriculum_planner: Agent,
    strategy_planner: Agent,
    synthesizer: Agent,
    learning_goal: str,
    available_time: str,
    skill_level: str = "Beginner",
) -> list[Task]:
    """Build the study planning task list.

    Args:
        curriculum_planner: Agent responsible for topic breakdown and sequencing.
        strategy_planner: Agent responsible for time allocation and practice design.
        synthesizer: Agent responsible for generating the final unified study plan.
        learning_goal: What the learner aims to achieve.
        available_time: The learner's available study time/duration.
        skill_level: Learner's current skill level (e.g. Beginner, Intermediate).

    Returns:
        An ordered list of 3 Task objects.
    """
    curriculum_task = Task(
        description=(
            f"Design a structured learning curriculum for the following learner profile:\n\n"
            f"- Learning Goal: {learning_goal}\n"
            f"- Current Skill Level: {skill_level}\n"
            f"- Available Time Frame: {available_time}\n\n"
            "Requirements:\n"
            "1. Deconstruct the learning goal into logical core topics and subtopics.\n"
            "2. Identify necessary prerequisites based on the starting skill level.\n"
            "3. Sequence topics strictly from foundational concepts to advanced applications.\n"
            "4. Define specific learning objectives for each topic."
        ),
        expected_output=(
            "A structured curriculum outline containing:\n"
            "- Identified Prerequisites\n"
            "- Ordered Topics & Key Subtopics\n"
            "- Specific Learning Objectives for each module"
        ),
        agent=curriculum_planner,
    )

    strategy_task = Task(
        description=(
            f"Create a practical study and time-allocation strategy based on the curriculum "
            f"from the previous step:\n\n"
            f"- Total Available Time: {available_time}\n"
            f"- Skill Level: {skill_level}\n\n"
            "Requirements:\n"
            "1. Allocate the available study time proportionally across all curriculum topics.\n"
            "2. Design specific, hands-on practice activities, coding/practical exercises, or mini-projects.\n"
            "3. Establish a spaced revision routine and knowledge checkpoints.\n"
            f"4. Keep the pace realistic and sustainable for a {skill_level} learner within {available_time}."
        ),
        expected_output=(
            "A study strategy document containing:\n"
            "- Time Allocation per topic/phase matching the total available time\n"
            "- Recommended Hands-on Practice Activities & Mini-Projects\n"
            "- Spaced Revision Schedule & Checkpoints"
        ),
        agent=strategy_planner,
        context=[curriculum_task],
    )

    synthesis_task = Task(
        description=(
            f"Synthesize the curriculum breakdown and study strategy into a single, cohesive, "
            f"and actionable study plan for: '{learning_goal}'.\n\n"
            "The final study plan must include:\n"
            "1. Learning Objectives: Clear targets the learner will hit.\n"
            "2. Ordered Topics: Step-by-step topic progression from basics to advanced.\n"
            f"3. Suggested Time Allocation: Practical distribution of the available time ({available_time}).\n"
            "4. Practice Activities: Concrete exercises and hands-on mini-projects.\n"
            "5. Revision Strategy: Spaced repetition and review schedule.\n"
            "6. Expected Outcome: Tangible milestone or capstone project marking completion.\n\n"
            "Format the output cleanly in readable Markdown with clear headings and checklists."
        ),
        expected_output=(
            "A complete, actionable Markdown study plan with:\n"
            "# Study Plan: <Learning Goal>\n\n"
            "## 1. Overview & Learning Objectives\n"
            "## 2. Prerequisites\n"
            "## 3. Curriculum Roadmap & Time Allocation\n"
            "## 4. Hands-on Practice Activities\n"
            "## 5. Revision & Retention Strategy\n"
            "## 6. Expected Outcome & Capstone Project"
        ),
        agent=synthesizer,
        context=[curriculum_task, strategy_task],
    )

    return [curriculum_task, strategy_task, synthesis_task]
