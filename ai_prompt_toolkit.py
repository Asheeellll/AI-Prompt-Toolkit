import os
import openai
from fpdf import FPDF

# ----------------------------
# CONFIG
# ----------------------------
PROMPT_FOLDER = "prompts"
OUTPUT_FOLDER = "example"

PROMPT_FILES = {
    "1": ("Prompt (Cheat Sheet Generator).txt", "cheat sheet"),
    "2": ("Prompt (Quiz Flashcard Generator).txt", "quiz"),
    "3": ("Prompt (Study Planner Generator).txt", "study plan")
}

# ----------------------------
# HELPER FUNCTIONS
# ----------------------------
def load_prompt(file_name):
    path = os.path.join(PROMPT_FOLDER, file_name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def replace_placeholders(prompt_text, topic, duration, hours):
    prompt_text = prompt_text.replace("{INSERT_TOPIC_HERE}", topic)
    prompt_text = prompt_text.replace("{INSERT_TOPICS_HERE}", topic)
    prompt_text = prompt_text.replace("{INSERT_DURATION_HERE}", duration)
    prompt_text = prompt_text.replace("{INSERT_HOURS_HERE}", hours)
    return prompt_text

def call_chatgpt(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_text}],
        temperature=0.5
    )
    return response.choices[0].message.content

def save_as_txt(file_name, content):
    path = os.path.join(OUTPUT_FOLDER, file_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✅] Saved TXT: {path}")

def save_as_pdf(file_name, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    for line in content.split('\n'):
        pdf.multi_cell(0, 8, line)
    
    path = os.path.join(OUTPUT_FOLDER, file_name)
    pdf.output(path)
    print(f"[✅] Saved PDF: {path}")

def generate_content(prompt_file, output_name, topic, duration, hours, save_pdf):
    prompt_text = load_prompt(prompt_file)
    prompt_text = replace_placeholders(prompt_text, topic, duration, hours)
    output = call_chatgpt(prompt_text)
    
    save_as_txt(f"{output_name}.txt", output)
    if save_pdf:
        save_as_pdf(f"{output_name}.pdf", output)

# ----------------------------
# MAIN MENU
# ----------------------------
if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    print("Select the prompt to run:")
    print("1 - Cheat Sheet")
    print("2 - Quiz / Flashcards")
    print("3 - Study Planner")
    print("4 - All prompts")
    
    choice = input("Enter your choice (1/2/3/4): ").strip()
    topic = input("Enter the topic: ")
    duration = input("Enter duration (e.g., '2 weeks'): ")
    hours = input("Enter hours per day (e.g., '2'): ")
    
    pdf_choice = input("Do you want the PDF to be generated? (y/n): ").strip().lower()
    save_pdf = pdf_choice == "y"

    if choice == "4":
        for key in ["1", "2", "3"]:
            prompt_file, output_name = PROMPT_FILES[key]
            generate_content(prompt_file, output_name, topic, duration, hours, save_pdf)
    elif choice in PROMPT_FILES:
        prompt_file, output_name = PROMPT_FILES[choice]
        generate_content(prompt_file, output_name, topic, duration, hours, save_pdf)
    else:
        print("[❌] Invalid choice. Exiting.")

    print("\n[🔥] Generation complete! Check the 'example/' folder for outputs.")
