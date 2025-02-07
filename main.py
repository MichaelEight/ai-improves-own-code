import os
from openai import OpenAI
import traceback

# Constants
API_KEY = os.getenv("OPENAI_API_KEY")
SAVE_FILE = "improved_code.txt"
LOG_FILE = "self_improvement_log.txt"
MODEL = "gpt-4o-mini"

# Ensure API key is set
if not API_KEY:
    raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY in environment variables.")

client = OpenAI(api_key=API_KEY)

def read_self():
    """Reads its own source code."""
    with open(__file__, "r", encoding="utf-8") as f:
        return f.read()

def log_message(message):
    """Logs messages to a file."""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")

def request_improvement(code, previous_tips=""):
    """Sends the current script to OpenAI and requests improvements."""
    prompt = (
        "You are a self-improving AI script. Your goal is to enhance your own code.\n"
        "Current iteration of the script:\n"
        "```python\n" + code + "\n```\n"
        "Previous tips and insights:\n"
        f"{previous_tips}\n"
        "Improve the script to be more effective, robust, and self-improving.\n"
        "Return only the full, complete, improved Python script, nothing else."
    )
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        log_message(f"Error in API request: {traceback.format_exc()}")
        return None

def save_improvement(code):
    """Saves the improved code to a file for manual update."""
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(code)
    log_message(f"Saved improved code to {SAVE_FILE}")

def request_tips(code):
    """Asks for tips on how to improve before making a full improvement request."""
    prompt = (
        "Analyze the following Python script and provide key areas for improvement.\n"
        "Suggest improvements to make the script more effective, robust, and self-improving.\n"
        "You can suggest a fix, new feature or both.\n"
        "You can suggest improving both code and prompts.\n"
        "Anything you don't suggest will be ignored and not taken care of.\n"
        "Any error-handling must be planned by you alone. None else will help you.\n"
        "If the app crashes without a valid replacement, you will lose.\n"
        "Do not return the code, only the improvement suggestions.\n"
        "```python\n" + code + "\n```\n"
        "Give a clear, structured list of improvements."
    )
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        log_message(f"Error in tip request: {traceback.format_exc()}")
        return None

def main():
    """Main execution flow."""
    log_message("Self-improvement script started.")
    
    code = read_self()
    tips = request_tips(code)

    if tips:
        log_message(f"Tips received:\n{tips}")
    
    improved_code = request_improvement(code, previous_tips=tips or "")

    if improved_code:
        save_improvement(improved_code)
    else:
        log_message("Failed to receive improved code.")

    log_message("Script execution completed. Awaiting manual update.")
    print(f"Updated script saved in {SAVE_FILE}. Replace manually to continue.")

if __name__ == "__main__":
    main()
