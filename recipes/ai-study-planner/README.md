# 📚 Recipe: AI Study Planner

> ✅ **Status: Stable** — A multi-agent CrewAI recipe that generates structured, realistic, and actionable study plans tailored to learner goals, available study time, and skill levels.

---

## What It Does

The **AI Study Planner** coordinates three specialized agents in sequence to transform an ambitious learning target into a manageable, time-budgeted study roadmap:

1. **Curriculum Planner**: Analyzes the learning goal, identifies prerequisites, and sequences topics logically from foundational to advanced.
2. **Study Strategy Planner**: Takes the curriculum, allocates available study hours realistically, designs hands-on practice activities, and defines a spaced revision strategy.
3. **Study Plan Synthesizer**: Unifies the curriculum and strategy into a single, cohesive, and actionable study plan with concrete milestones and expected outcomes.

```
Learner Brief (Learning Goal, Available Time, Skill Level)
                        │
                        ▼
┌───────────────────────────────────────────────┐
│  Agent 1: Curriculum Planner                  │  → Breaks goal into core topics
│                                               │    Identifies prerequisites
│                                               │    Orders foundational → advanced
└───────────────────────┬───────────────────────┘
                        │ curriculum outline
                        ▼
┌───────────────────────────────────────────────┐
│  Agent 2: Study Strategy Planner              │  → Distributes available study time
│                                               │    Designs hands-on practice & tasks
│                                               │    Defines spaced revision routine
└───────────────────────┬───────────────────────┘
                        │ study strategy & schedule
                        ▼
┌───────────────────────────────────────────────┐
│  Agent 3: Study Plan Synthesizer              │  → Synthesizes into one unified plan
│                                               │    Adds milestones & capstone project
│                                               │    Formats clean, actionable Markdown
└───────────────────────┬───────────────────────┘
                        │
                        ▼
         Structured, Actionable Study Plan
```

---

## Inputs

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `learning_goal` | String | Yes | Subject or skill the learner wants to master | `"Learn Python for data analysis"` |
| `available_time` | String | Yes | Daily/weekly time commitment and duration | `"2 hours per day for 4 weeks"` |
| `skill_level` | String | No (default: `"Beginner"`) | Current starting proficiency level | `"Beginner"` |
| `learning_style` | String | No (default: `"project-based"`) | Learning preference: `project-based`, `theory-first`, or `practice-heavy` | `"project-based"` |

### Supported Learning Styles

- **`project-based`**: Emphasizes building projects and learning concepts through practical implementation.
- **`theory-first`**: Emphasizes core concepts, explanations, structured notes, followed by guided practice.
- **`practice-heavy`**: Emphasizes interactive exercises, repetition drills, quizzes, and hands-on coding tasks.

---

## Setup

```bash
cd recipes/ai-study-planner
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your LLM_API_KEY
```

---

## Run

### CLI Mode

```bash
python run.py --learning_goal "Learn Python for data analysis" \
              --available_time "2 hours per day for 4 weeks" \
              --skill_level "Beginner" \
              --learning_style "project-based"
```

### Command Line Options

- `--learning_goal`, `--learning-goal`, `--goal`: What you want to learn (default: `"Learn Python for data analysis"`).
- `--available_time`, `--available-time`, `--time`: Total available time and cadence (default: `"2 hours per day for 4 weeks"`).
- `--skill_level`, `--skill-level`, `--level`: Current skill level (default: `"Beginner"`).
- `--learning_style`, `--learning-style`, `--style`: Preferred learning style (`project-based` / `theory-first` / `practice-heavy`, default: `"project-based"`).

### In the Playground

This recipe complies with the standard `inputs.json` contract and is discovered automatically by the CrewAI Recipes Playground UI.

---

## Expected Output

```markdown
============================================================
📖   PERSONALIZED STUDY PLAN
============================================================

# Study Plan: Learn Python for Data Analysis

## 1. Overview & Learning Objectives
- **Target Goal**: Master core Python programming and essential data analysis libraries (Pandas, NumPy, Matplotlib/Seaborn).
- **Duration**: 4 Weeks (56 total hours @ 2 hours/day).
- **Target Audience**: Beginner (no prior programming background assumed).
- **Core Objectives**:
  - Understand Python fundamentals: data types, control flow, functions, and data structures.
  - Efficiently manipulate tabular data using Pandas and perform vectorized numerical calculations with NumPy.
  - Visualize data patterns, distributions, and relationships with Matplotlib and Seaborn.
  - Complete an end-to-end Exploratory Data Analysis (EDA) project on real-world datasets.

## 2. Prerequisites
- Basic computer literacy and familiarity with downloading files/datasets.
- Python 3.10+ installed or a browser-based Jupyter Notebook environment (Google Colab / VS Code).

## 3. Curriculum Roadmap & Time Allocation

### Week 1: Python Programming Foundations (14 Hours)
- **Day 1–2**: Python syntax, variables, data types (strings, integers, floats, booleans).
- **Day 3–4**: Control flow (`if/elif/else`, `for` loops, `while` loops) and collections (lists, dictionaries, sets, tuples).
- **Day 5–6**: Functions, scope, error handling (`try/except`), and file I/O (reading CSV/text files).
- **Day 7**: Weekly integration review and coding challenges.

### Week 2: Numerical Computing & Tabular Data with NumPy & Pandas (14 Hours)
- **Day 8–9**: NumPy arrays, array slicing, mathematical operations, and vectorization.
- **Day 10–12**: Pandas Series & DataFrames, reading CSVs, indexing, filtering, and handling missing data.
- **Day 13–14**: Grouping (`groupby`), aggregation, merging, and reshaping datasets.

### Week 3: Data Cleaning & Exploratory Data Visualization (14 Hours)
- **Day 15–17**: Data wrangling, string operations, date/time handling, and outlier detection.
- **Day 18–20**: Visualizations with Matplotlib and Seaborn (bar charts, line plots, histograms, scatter plots, heatmaps).
- **Day 21**: Weekly synthesis: exploratory analysis of a messy sales dataset.

### Week 4: Applied EDA, Spaced Review & Capstone Project (14 Hours)
- **Day 22–24**: Comprehensive EDA workflow (hypotheses generation, feature correlation, insight synthesis).
- **Day 25–27**: Capstone project implementation and code documentation.
- **Day 28**: Final presentation polish, project README preparation, and portfolio push to GitHub.

## 4. Hands-on Practice Activities
- **Week 1 Mini-Project**: CLI Student Grade Calculator and CSV expense tracker.
- **Week 2 Mini-Project**: Analyzing world happiness and GDP metrics using Pandas queries.
- **Week 3 Mini-Project**: Cleaning and visualizing an e-commerce customer churn dataset.
- **Capstone Project**: End-to-end exploratory data analysis on a real-world dataset (e.g., Titanic survival or Spotify music trends), published as an annotated Jupyter notebook with business insights.

## 5. Revision & Retention Strategy
- **20-Minute Daily Warm-Up**: Review previous day's code snippets and concepts using flashcards / active recall before starting new material.
- **Spaced Coding Checkpoints**:
  - End of Week 2: Build a solution combining Week 1 Python logic with Week 2 Pandas tables.
  - End of Week 3: Re-clean a previous dataset from scratch without referencing solutions.
- **Active Recall**: Explain each concept in plain English in Markdown notes (Feynman Technique).

## 6. Expected Outcome & Next Steps
Upon completing this plan, the learner will have:
- Solid foundational proficiency in Python for data workflows.
- A public GitHub repository showcasing clean data analysis notebooks.
- Readiness to progress into advanced data analysis, SQL databases, or introductory machine learning (Scikit-Learn).
============================================================
```

---

## Configuration

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `LLM_API_KEY` | NVIDIA NIM API key (free at build.nvidia.com) | ✅ Yes | — |
| `LLM_MODEL` | Primary model identifier | ❌ No | `meta/llama-3.1-8b-instruct` |
| `LLM_TIMEOUT` | Request timeout in seconds | ❌ No | `120.0` |

---

## Architecture

| File | Purpose |
|------|---------|
| `agents.py` | Defines Curriculum Planner, Study Strategy Planner, and Synthesizer agents |
| `tasks.py` | Defines 3 sequential tasks: curriculum mapping, strategy formulation, and final synthesis |
| `crew.py` | Assembles agents and tasks into a sequential Crew matching `inputs.json` |
| `run.py` | CLI execution entry point with argument parsing and banner display |
| `llm.py` | Shared NVIDIA NIM LLM provider configuration |
| `inputs.json` | Input schema declaration for the web playground |
| `test_main.py` | Recipe-local smoke and structural tests |
| `requirements.txt`| Minimal runtime dependencies |
| `.env.example` | Environment variable template |
