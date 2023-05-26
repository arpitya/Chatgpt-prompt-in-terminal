import openai

# Define OpenAI API key
openai.api_key = "Enter your API key"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input('Enter new prompt: ')

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion. choices[0].text
print(response)
