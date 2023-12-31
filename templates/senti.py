from textblob import TextBlob
import nltk
from googlesearch import Search

# Download the necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_sentiment(diary_text):
    # Analyze the sentiment of the diary text
    blob = TextBlob(diary_text)
    sentiment = blob.sentiment.polarity  # returns a value between -1 and 1

    # Define a wider range of adjectives for different sentiments
    adjectives = {
        'very_positive': ['ecstatic', 'delighted', 'elated'],
        'positive': ['happy', 'content', 'cheerful'],
        'quite_happy': ['joyful', 'blissful', 'upbeat'],
        'mildly_happy': ['pleased', 'satisfied', 'smiling'],
        'neutral': ['ordinary', 'calm', 'average'],
        'mildly_negative': ['displeased', 'concerned', 'unhappy'],
        'negative': ['sad', 'frustrated', 'disappointed'],
        'quite_negative': ['angry', 'irritated', 'miserable'],
        'very_negative': ['depressed', 'despairing', 'hopeless'],
        'extremely_negative': ['hateful', 'enraged', 'agonized']
    }

    # Map sentiment scores to sentiment categories
    sentiment_categories = {
        'extremely_negative': (-1.0, -0.9),
        'very_negative': (-0.9, -0.7),
        'quite_negative': (-0.7, -0.5),
        'negative': (-0.5, -0.3),
        'mildly_negative': (-0.3, -0.1),
        'neutral': (-0.1, 0.1),
        'mildly_happy': (0.1, 0.3),
        'quite_happy': (0.3, 0.5),
        'positive': (0.5, 0.7),
        'very_positive': (0.7, 1.0)
    }

    # Determine the sentiment category based on sentiment score
    sentiment_category = None
    for category, (lower_bound, upper_bound) in sentiment_categories.items():
        if lower_bound <= sentiment <= upper_bound:
            sentiment_category = category
            break

    # Perform a Google search for music based on mood adjectives
    if sentiment_category:
        mood_adjectives = adjectives[sentiment_category]
        query = f"Top 3 songs from youtube to listen to when feeling {', '.join(mood_adjectives)}"
    else:
        mood_adjectives = adjectives['neutral']
        query = f"Top 3 songs from youtube to listen to when feeling {', '.join(mood_adjectives)}"

    # Perform the Google search and filter playable music links
    print(f"Searching for music recommendations based on your mood: {', '.join(mood_adjectives)}")
    search_results = Search(query)
    search_results = search_results.results

    # Filter links that are directly playable music (e.g., YouTube, Spotify)
    playable_music_links = []
    for result in search_results:
        link = result.url
        if 'youtube.com' in link or 'spotify.com' in link:
            playable_music_links.append({'title': result.title, 'link': link})

    return playable_music_links
