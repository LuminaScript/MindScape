import openai

# Set your OpenAI GPT-3 API key
openai.api_key = '******'

def generate_short_story(noun1, noun2, noun3):
    prompt = f"Write a short story about {noun1}, {noun2}, and {noun3}."
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the text-davinci-002 engine
        prompt=prompt,
        max_tokens=100  # Set the maximum number of tokens for the response
    )
    return response.choices[0].text.strip()

# Example usage
noun1 = "ocean"
noun2 = "space"
noun3 = "whale"

short_story = generate_short_story(noun1, noun2, noun3)
print(short_story)
