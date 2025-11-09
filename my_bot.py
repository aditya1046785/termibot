#!/usr/bin/env python3


import google.generativeai as genai
import sys
import os
import json
from pathlib import Path

# --- Configuration ---
# History file ka path set karte hain (e.g., /home/aditya/.termibot_history.json)
HISTORY_FILE = Path.home() / ".termibot_history.json"
MAX_HISTORY_LENGTH = 10 # Kitni purani baatein yaad rakhni hain (User + Bot messages)

# --- Step A: API KEY CONFIGURATION ---
# --- Step A: API KEY CONFIGURATION ---
try:
    MY_API_KEY = os.getenv("GEMINI_API_KEY")  # Securely fetch API key from environment
    if not MY_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    genai.configure(api_key=MY_API_KEY)
except Exception as e:
    print(f"Error: API Key configure nahi ho payi. Check your key. Details: {e}")
    sys.exit(1)

# --- History Management Functions ---
def load_history():
    """JSON file se chat history load karta hai."""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return [] # Agar file khali ya corrupt hai
    return []

def save_history(history):
    """Chat history ko JSON file me save karta hai (serializable format me)."""
    serializable_history = []
    for item in history:
        # Har special 'Content' object ko ek simple dictionary me convert karte hain
        # jise JSON samajh sake.
        serializable_history.append({
            'role': item.role,
            'parts': [part.text for part in item.parts]
        })

    with open(HISTORY_FILE, 'w') as f:
        # History ko limit me rakhte hain
        if len(serializable_history) > MAX_HISTORY_LENGTH:
            serializable_history = serializable_history[-MAX_HISTORY_LENGTH:]
        json.dump(serializable_history, f, indent=2)

# --- Step B: UPGRADED PROMPT ENGINEERING ---
def get_response_from_gemini(user_query, history):
    # Model ko set karte hain, latest use karna best hai
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Ye hai humara naya, smarter prompt!
    engineered_prompt = f"""
    You are a Linux Mint Terminal assistant named TermiBot.
    Your user needs direct, practical, and concise answers formatted for a terminal.
    - If the user asks for a command, provide the most common form of the command.
    - Briefly explain its main purpose.
    - Do not add extra formatting like triple backticks (```,**,etc) unless it's part of the command its>
    - Provide 1-2 practical examples or common use-case flags (e.g., `ls -lh`, `grep -i 'pattern' filename`).
    - Keep the entire response concise. Avoid conversational fillers like "Sure, here is..."

    User's Query: "{user_query}"
    """
    
    # History ke saath chat session shuru karte hain
    chat = model.start_chat(history=history)
    
    try:
        response = chat.send_message(engineered_prompt)
        clean_text = response.text.strip()
        return clean_text, chat.history # Response ke saath updated history bhi lautaate hain
    except Exception as e:
        return f"API se response laane me error aayi: {e}", history

# --- Step C: MAIN LOGIC with HISTORY ---
def main():
    # Purani history load karo
    chat_history = load_history()

    if len(sys.argv) > 1:
        # One-shot command mode
        user_query = " ".join(sys.argv[1:])
        bot_response, updated_history = get_response_from_gemini(user_query, chat_history)
        print(bot_response)
        # History ko save karo
        save_history(updated_history)
    else:
        # Interactive mode
        print("🚀 TermiBot v2.0 Interactive Mode! (Memory Enabled) 🚀")
        while True:
            user_input = input("You > ")
            if user_input.lower() in ['exit', 'quit']:
                print("TermiBot > Chalo, milte hain fir!")
                break
            
            bot_response, updated_history = get_response_from_gemini(user_input, chat_history)
            print(f"TermiBot > {bot_response}")
            # Har message ke baad history ko update aur save karo
            chat_history = updated_history
            save_history(chat_history)

if __name__ == "__main__":
    main()