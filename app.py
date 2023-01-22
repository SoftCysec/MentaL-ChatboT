import os
from dotenv import load_dotenv
from flask import Flask, request
import openai

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["POST"])
def chatbot():
    user_input = request.form["text"]
    prompts = [
        "Mental health consultation: ",
        "Mental symptoms: ",
        "Mental health history: ",
        "Diagnosis: ",
        "Treatment options: ",
        "Therapy options: ",
        "Medication options: ",
        "Self-help strategies: ",
        "Simplified English: ",
        "Feeling today: ",
        "Stressors in your life: ",
        "Support system: "
    ]
    prompt = prompts[0]
    if "symptoms" in user_input.lower():
        prompt = prompts[1]
    elif "mental health history" in user_input.lower():
        prompt = prompts[2]
    elif "diagnosis" in user_input.lower():
        prompt = prompts[3]
    elif "treatment" in user_input.lower():
        prompt = prompts[4]
    elif "therapy" in user_input.lower():
        prompt = prompts[5]
    elif "medication" in user_input.lower():
        prompt = prompts[6]
    elif "self-help" in user_input.lower():
        prompt = prompts[7]
    elif "english" in user_input.lower():
        prompt = prompts[8]
    elif "feeling" in user_input.lower():
        prompt = prompts[9]
    elif "stress" in user_input.lower():
        prompt = prompts[10]
    elif "support" in user_input.lower():
        prompt = prompts[11]

    prompt = prompt + user_input
    temperature = 0.5
    max_tokens = 100
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, temperature=temperature, max_tokens=max_tokens, n=1)
    message = completions.choices[0].text
    return message

if __name__ == "__main__":
    app.run()
