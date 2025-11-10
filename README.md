# 🤖 TermiBot - The Cross-Platform CLI Co-Pilot

TermiBot is a fast, memory-enabled, terminal-based assistant powered by the **Gemini API**. It is designed to provide concise, practical command-line answers for **Linux, macOS, and Windows** environments, serving as your intelligent command-line co-pilot.

---

## ✨ Key Features

* **Intelligent Terminal Answers:** Provides direct, concise command-line output suitable for execution.
* **Dynamic OS Awareness:** The bot automatically detects the user's operating system (Linux, macOS, or Windows) and provides **commands specific to that environment** (e.g., `dir` for Windows, `ls` for Linux/macOS).
* **Zero-Setup Key Management:** The Gemini API Key is requested **only once** upon the first run and is securely saved to a hidden file (`~/.termibot_api_key`), eliminating the need for environment variable configuration.
* **Contextual Memory:** Remembers the last 10 messages for continuous, contextual conversations (history saved in `~/.termibot_history.json`).
* **Dual Mode:** Supports both one-shot query mode (`bot "query"`) and interactive chat mode.
* **Clean Setup:** Utilizes Python Virtual Environments (`venv`) for dependency isolation and zero system clutter.

---

## 🛠️ Installation and Setup

### Prerequisites

1.  **Python 3** (version 3.8 or higher) installed on your system.
2.  A **Gemini API Key**. You can obtain one from [Google AI Studio].

### Step-by-Step Setup (Universal)

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/aditya1046785/termibot.git
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

4.  **Deactivate Venv:** (Ensure you exit the environment before setting up global shortcuts)
    ```bash
    deactivate
    ```

---

## 🚀 Usage Guide

TermiBot is designed to be run globally from any directory. Follow the steps for your specific operating system.

### 🐧 macOS / Linux (The `bot` Command Method)

This method creates a symbolic link in your local binary path (`~/.local/bin/`), allowing the bot to be called simply as `bot`.

1.  **Create the `bot` Command Shortcut:**
    ```bash
    # 1. Create the symbolic link:
    ln -s "$(pwd)/my_bot.py" ~/.local/bin/bot
    
    # 2. Make the link executable:
    chmod +x ~/.local/bin/bot
    ```

2.  **Run the Bot:**
    * **First Run:** Execute `bot`. The script will prompt you to enter your Gemini API Key and securely save it for future use.
    * **One-Shot Query:**
        ```bash
        bot "command to list running processes"
        # Output will be Linux/macOS specific, e.g., 'ps aux'
        ```
    * **Interactive Chat:**
        ```bash
        bot
        ```

### 🪟 Windows (Using the `termibot.bat` File)

For Windows users, use the provided `termibot.bat` file, which automatically manages the virtual environment for you.

1.  **Run the Bot (from the project directory):**
    * **First Run:** Execute `termibot`. The script will prompt you to enter your Gemini API Key and securely save it for future use.
    * **One-Shot Query:**
        ```bash
        termibot "windows command to list services"
        # Output will be Windows specific, e.g., using 'Get-Service'
        ```
    * **Interactive Chat:**
        ```bash
        termibot
        ```
    *(Note: To run `termibot` from any directory on Windows, add the project path to your system's Environment Variables (PATH).)*

---