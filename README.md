Azure Open AI Simple TK App 

## Overview
This application is an interactive chat application that utilizes an Azure Open Ai deployment. Just The app provides a user interface with TK for sending queries and receiving responses from the model. 

<img src="media/chat.png" alt="Chat preview" width="512">

## Files
- `main.py`: The entry point for the application. It initializes and runs the chat application.
- `chat.py`: Contains the `Chat` class, which sets up the GUI for the chat application using Tkinter and handles the interaction logic.
- `env.template`: A template for setting up environment variables required for the application, such as API keys and endpoint URLs.
- `completion.py`: Handles the Azure Open AI completion .

## Prerequisites
- Python 3.x
- `tkinter`, `dotenv`, `openai`  libraries.
- An Azure account with a deployed Azure Open AI model.
- Azure OpenAI API key.


# Getting Started

# WINDOWS
1. Create a Virtual Environment (`python3 -m venv /path/to/new/virtual/environment`)
2. Activate Virtual Environment (`path\to\venv\Scripts\activate.bat`)
3. Install requirements.txt (`pip install -r requirements.txt`)


## UNIX
1. Create a Virtual Environment (`python3 -m venv <environment name>`)
2. Activate Virtual Environment (`source <environment name>/bin/activate`)
3. Install requirements.txt (`pip3 install -r requirements.txt`)



## Usage
1. Run `main.py` to start the chat application: `python main.py`.
2. Enter your queries in the application's chat window.
3. Responses from the GPT model will be displayed in the chat window.

## Configuration
- Environment variables should be set as per `env.template`.

## Support
For any issues or queries, please open an issue in the repository or contact the development team.
