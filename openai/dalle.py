import openai

def generate_image_from_story(story):
<<<<<<< HEAD
    openai.api_key = '**********'  
=======
    openai.api_key = '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'  # Replace with your OpenAI API key
>>>>>>> 86c4ef0 (finished)

    try:
        # Assuming DALL-E API has an endpoint similar to GPT-3 for image generation
        response = openai.Image.create(
            prompt=story,
            n=1,  # Number of images to generate
            size="1024x1024"  # Size of the image
        )

        # Assuming the response contains a URL or data for the generated image
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
short_story = "A serene landscape with mountains in the background and a clear lake in the foreground under a twilight sky."
image_url = generate_image_from_story(short_story)
print(f"Generated image URL: {image_url}")
