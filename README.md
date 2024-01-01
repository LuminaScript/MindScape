# MindScape

## Project Overview

MindScape is an innovative web application that offers a unique blend of therapeutic and creative experiences, leveraging the power of AI. It serves as a meta-universe spiritual space, providing users with an immersive environment for relaxation and self-discovery. The project integrates advanced AI technologies to simulate aspects of offline psychological therapy, making mental wellness more accessible and engaging.

## Aim

MindScape aims to offer an alternative to traditional offline psychological therapy, integrating cutting-edge AI to create a safe, relaxing, and therapeutic digital space. It's a platform where technology meets mental wellness, providing users with tools to explore their inner world, express emotions, and engage with AI-driven creative processes.

## Features

### Sentiment Diary Analysis

The Sentiment Diary Analysis feature allows users to express their thoughts and feelings in a diary entry. The application then analyzes the sentiment of the text using the `TextBlob` library, categorizing the emotions into various degrees from extremely positive to extremely negative.

#### Code Description

```python
def analyze_sentiment(diary_text):
    # Analyze the sentiment of the diary text using TextBlob
    blob = TextBlob(diary_text)
    sentiment = blob.sentiment.polarity  # returns a value between -1 and 1

    # Define adjectives for different sentiments
    adjectives = {
        # ...adjectives dictionary...
    }

    # Map sentiment scores to categories
    sentiment_categories = {
        # ...sentiment_categories dictionary...
    }

    # Determine the sentiment category and perform a Google search for music
    # based on mood adjectives
    # ...rest of the function...
```

### AI Sandtable
The AI Sandtable feature offers an interactive and creative outlet for users. They can select spiritual words, which the application then uses to generate a short story and a corresponding image. This feature employs OpenAI's GPT-3 for story generation and DALL-E for image creation, showcasing the synergy between storytelling and visual art.

## Conclusion

MindScape stands out as a digital haven for relaxation, creativity, and emotional exploration. Its combination of sentiment analysis, storytelling, and visual artistry opens up new possibilities in the realm of digital therapy and personal well-being.
