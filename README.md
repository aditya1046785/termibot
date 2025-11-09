# 🤖 TermiBot - The Intelligent Command Line Assistant

TermiBot is a fast, memory-enabled, terminal-based assistant that uses the Gemini API to provide concise, practical Linux commands and explanations, just like a helpful co-pilot.

---

## ✨ Features

* **Intelligent Terminal Answers:** Provides direct command-line answers (no verbose chat).
* **Memory Enabled:** Remembers the last 5 questions for context (using `.termibot_history.json`).
* **Dual Mode:** Works in one-shot mode (`bot "query"`) and interactive chat mode.
* **Clean Setup:** Uses Python Virtual Environments for zero system clutter.

---

## 🛠️ Installation (The Quick Way - Recommended)

This method sets up TermiBot so you can run it from anywhere in your terminal using just the command `bot`.

### Prerequisites

1.  **Python 3** (3.8+) installed on your system.
2.  A **Gemini API Key**. Get one from [Google AI Studio].

### Step-by-Step Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/aditya1046785/termibot.git
    cd termibot
    ```

2.  **Create and Activate Virtual Environment (venv):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the `bot` Command Shortcut (Crucial Step!):**
    This step creates the executable link to your script in your local command path (`~/.local/bin/`).

    ```bash
    # Ensure you are inside the 'termibot' directory
    # 1. Create the link:
    ln -s "$(pwd)/my_bot.py" ~/.local/bin/bot
    
    # 2. Make it executable:
    chmod +x ~/.local/bin/bot
    
    # 3. Deactivate the venv:
    deactivate
    ```

5.  **Set Your API Key (Security First!):**
    To use the bot, you **must** set your API key as an environment variable in your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.).

    *Add this line to the end of the file:*
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
    *Apply the changes:*
    ```bash
    source ~/.bashrc  # or source ~/.zshrc
    ```

---

## 🚀 How to Use TermiBot

Once set up, you can run `bot` from any directory.

### 1. One-Shot Command Mode

For quick answers:

```bash
bot "how to search for the word error in all log files"
# Output: grep -r 'error' *.log