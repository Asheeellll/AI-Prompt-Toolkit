AI-Prompt-Toolkit

Reusable AI Prompts to Generate Cheat Sheets, Quizzes, and Study Planners

Project Overview

AI-Prompt-Toolkit is a reusable prompt engineering project that automates the creation of educational and productivity content.
It demonstrates advanced prompt engineering skills and produces:

Cheat Sheets – concise one-page summaries with key points and examples.

Quizzes / Flashcards – multiple-choice questions or flashcards for rapid revision.

Study Planners – personalized weekly or monthly schedules based on topics, duration, and daily study hours.

Folder Structure
AI-PROMPT-TOOLKIT/
├── example/        # Generated outputs
│   ├── cheat sheet.txt / .pdf
│   ├── quiz.txt / .pdf
│   └── study plan.txt / .pdf
└── prompts/        # Reusable prompt templates
    ├── Prompt (Cheat Sheet Generator).txt
    ├── Prompt (Quiz Flashcard Generator).txt
    └── Prompt (Study Planner Generator).txt

How to Use
1. Python Script (Recommended – Automated)

Ensure dependencies are installed:

pip install openai fpdf python-dotenv


Set your OpenAI API key (recommended via environment variable or .env file):

setx OPENAI_API_KEY "YOUR_API_KEY_HERE"   # Windows CMD
# or PowerShell
$env:OPENAI_API_KEY="YOUR_API_KEY_HERE"


Run the script:

python ai_prompt_toolkit.py


Follow prompts:

Select which generator to run (Cheat Sheet, Quiz, Study Planner, or All).

Enter topic, duration, and daily study hours.

Choose whether to generate PDFs.

Check example/ folder for outputs.

2. Manual Prompt Usage

Open the relevant prompt in prompts/ folder.

Replace placeholders:

{INSERT_TOPIC_HERE} for Cheat Sheet / Quiz

{INSERT_TOPICS_HERE}, {INSERT_DURATION_HERE}, {INSERT_HOURS_HERE} for Study Planner

Copy into ChatGPT and run.

Save outputs in example/ as .txt or export as PDF.

Demo Outputs

example/cheat sheet.txt / .pdf – Sample cheat sheet

example/quiz.txt / .pdf – Sample quiz/flashcards

example/study plan.txt / .pdf – Sample study plan

Skills Demonstrated

Advanced Prompt Engineering

AI Content Automation

Educational / Productivity Tool Design

Safe API Key Handling

Notes

Fully reusable: replace topics, syllabus, or study parameters to generate new outputs.

Menu-driven script supports optional PDF export and dynamic prompt selection.

API key is never stored in code when using environment variables or .env.
