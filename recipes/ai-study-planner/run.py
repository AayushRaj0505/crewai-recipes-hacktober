"""
AI Study Planner Recipe — run.py

CLI entry point for running the AI study planner recipe.

Usage:
    python run.py --learning_goal "Learn Python for data analysis" \
                  --available_time "2 hours per day for 4 weeks" \
                  --skill_level "Beginner" \
                  --learning_style "project-based"
"""

import argparse
import os
import sys

from dotenv import load_dotenv

load_dotenv()

from crew import build_crew  # noqa: E402


def check_env() -> None:
    """Preflight environment check for required API key."""
    api_key = os.getenv("LLM_API_KEY") or os.getenv("NVIDIA_API_KEY")
    if not api_key:
        print("❌ Error: Missing API key.", file=sys.stderr)
        print(
            "   Please set LLM_API_KEY or NVIDIA_API_KEY in your .env file or environment.",
            file=sys.stderr,
        )
        print("   Get a free key at https://build.nvidia.com", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Parse CLI arguments and run the study planner crew."""
    parser = argparse.ArgumentParser(
        description="Run AI Study Planner Recipe with NVIDIA NIM"
    )
    parser.add_argument(
        "--learning_goal",
        "--learning-goal",
        "--goal",
        dest="learning_goal",
        type=str,
        default="Learn Python for data analysis",
        help="What you want to learn (e.g. 'Learn Python for data analysis')",
    )
    parser.add_argument(
        "--available_time",
        "--available-time",
        "--time",
        dest="available_time",
        type=str,
        default="2 hours per day for 4 weeks",
        help="Available study time (e.g. '2 hours per day for 4 weeks')",
    )
    parser.add_argument(
        "--skill_level",
        "--skill-level",
        "--level",
        dest="skill_level",
        type=str,
        default="Beginner",
        help="Current skill level (e.g. 'Beginner', 'Intermediate', 'Advanced')",
    )
    parser.add_argument(
        "--learning_style",
        "--learning-style",
        "--style",
        dest="learning_style",
        type=str,
        default="project-based",
        choices=["project-based", "theory-first", "practice-heavy"],
        help="Preferred learning style (project-based / theory-first / practice-heavy)",
    )

    args = parser.parse_args()
    check_env()

    print("\n📚  AI Study Planner — Building Personalized Roadmap\n")
    print(f"   Learning Goal  : {args.learning_goal}")
    print(f"   Available Time : {args.available_time}")
    print(f"   Skill Level    : {args.skill_level}")
    print(f"   Learning Style : {args.learning_style}\n")
    print("─" * 60)

    crew = build_crew(
        learning_goal=args.learning_goal,
        available_time=args.available_time,
        skill_level=args.skill_level,
        learning_style=args.learning_style,
    )
    result = crew.kickoff()

    print("\n" + "═" * 60)
    print("📖   PERSONALIZED STUDY PLAN")
    print("═" * 60)
    print(result)
    print("═" * 60 + "\n")


if __name__ == "__main__":
    main()
