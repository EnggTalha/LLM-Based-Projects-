# GPT-powered Streamlit Chatbot

This is a simple Streamlit app that lets users interact with OpenAI's GPT-3 model.

## Features

- Users can input text and get responses from GPT-3.
- Built using Streamlit and OpenAI API.

## Requirements

- Python 3.x
- Streamlit
- OpenAI Python package

## Setup Instructions

1. Clone the repository or download the files.
2. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

3. Add your OpenAI API key to your environment variables:

    - On Linux/macOS: 
        ```
        export OPENAI_API_KEY="your_openai_key"
        ```
    - On Windows (Command Prompt):
        ```
        set OPENAI_API_KEY="your_openai_key"
        ```

4. Run the app using Streamlit:

    ```
    streamlit run app.py
    ```

## How It Works

- The `app.py` file is the main entry point for the Streamlit app.
- The `main.py` file contains the function that interacts with the OpenAI API.

## Usage

Enter a prompt into the text box, and the GPT model will generate a response. This is a simple chatbot that demonstrates how to use OpenAI's API in a web app.
