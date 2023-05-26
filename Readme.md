# OpenAI Chatbot Code

This repository contains code that utilizes the OpenAI API to generate responses using the OpenAI GPT-3.5 model. The code allows you to interact with the model and generate responses based on a given prompt.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your machine.
- OpenAI Python library installed. You can install it using the following command:
``` pip install openai ```

## Setup

1. Clone the repository:<br>
```git clone https://github.com/arpitya/Chatgpt-prompt-in-terminal```

2. Set up OpenAI API key:
- Go to the OpenAI website and create an account (if you don't have one already).
- Obtain your API key from the OpenAI dashboard.
- Replace `enter your api key` in the code with your actual API key.

## Usage

1. Open the code file (e.g., `chatbot.py`) in your preferred Python IDE or text editor.

2. Set the model engine and prompt:
- Replace `text-davinci-003` in the code with the desired model engine. You can refer to the OpenAI documentation for available engine options.
- Set the `prompt` variable to the desired text prompt for generating a response. The prompt can be entered during runtime or provided as a fixed value.

3. Run the code:
- Execute the code file (`chatbot.py`) using the Python interpreter.

4. View the response:
- The generated response will be displayed in the console output.

## Additional Notes

- The code uses the OpenAI Python library to interact with the OpenAI API. You can refer to the library's documentation for more advanced usage and options.
- Adjust the parameters in the `openai.Completion.create()` method to modify the behavior of the response generation. For example, you can change the `max_tokens`, `temperature`, and `n` values.
- Remember to handle any exceptions or errors that may occur during API communication or execution.
## Authors
- [Arpitya Kumar Singh ](https://github.com/arpitya)