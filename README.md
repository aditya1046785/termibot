# 🤖 TermiBot - The Cross-Platform CLI Co-Pilot

TermiBot is a fast, memory-enabled, terminal-based assistant that uses the Gemini API. It is designed to provide concise, practical command-line answers for **Linux, macOS, and Windows** environments, acting as your smart co-pilot.

---

## ✨ Features

* **Intelligent Terminal Answers:** Provides direct, concise command-line output.
* **Dynamic OS Awareness:** Automatically detects the user's operating system (using Python's `sys.platform`) and provides **specific commands** for Linux, macOS, or Windows (CMD/PowerShell).
* **Memory Enabled:** Remembers the last 10 messages for contextual conversations (history saved in `~/.termibot_history.json`).
* **Dual Mode:** Works in one-shot mode (`bot "query"`) and interactive chat mode.
* **Clean Setup:** Uses Python Virtual Environments (`venv`) for zero system clutter.

---

## 🛠️ Installation & Setup

### Prerequisites

1.  **Python 3** (3.8+) installed on your system.
2.  A **Gemini API Key**. Get one from [Google AI Studio].

### Step-by-Step Setup (Universal)

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/aditya1046785/termibot.git](https://github.com/aditya1046785/termibot.git)
    cd termibot
    ```

2.  **Create and Activate Virtual Environment (venv):**

    * **Linux/macOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows (CMD/PowerShell):**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Your API Key (CRITICAL):**
    You **must** set your Gemini API key as an environment variable (`GEMINI_API_KEY`).

    * **Linux/macOS (.bashrc/.zshrc):**
        ```bash
        export GEMINI_API_KEY="YOUR_API_KEY_HERE"
        source ~/.bashrc  # or source ~/.zshrc
        ```
    * **Windows (Permanent Variable):**
        Set the environment variable `GEMINI_API_KEY` through the **System Properties** GUI.

---

## 🚀 How to Use TermiBot

The method you use to run TermiBot depends on your operating system.

### 🐧 macOS / Linux (The `bot` Shortcut Method - Recommended)

This sets up a simple `bot` command that runs from any directory.

1.  **Create the `bot` Command Shortcut:**
    This command links your script to your command path (`~/.local/bin/`).

    ```bash
    # 1. Create the link:
    ln -s "$(pwd)/my_bot.py" ~/.local/bin/bot
    
    # 2. Make it executable:
    chmod +x ~/.local/bin/bot
    
    # 3. Deactivate the venv:
    deactivate
    ```

2.  **Run the Bot:**
    * **One-Shot:** `bot "command to list disk space"`
    * **Interactive:** `bot`

---

### 🪟 Windows (Using the `termibot.bat` File)

For Windows users, use the provided `termibot.bat` file which automatically handles venv activation and script execution.

1.  **Run the Bot (from the project directory):**
    * **One-Shot:**
        ```bash
        termibot "windows command to list services"
        ```
        *(The bot will automatically provide Windows-specific output)*
    * **Interactive:**
        ```bash
        termibot
        ```

### 💡 Manual Method (All Platforms)

If you skip the shortcut, you can always run the script manually:

```bash
# First, activate the environment:
 (Linux/Mac: source venv/bin/activate)
 |
 (Windows: .\venv\Scripts\activate)

# Then run the script:
python my_bot.py "your query here"