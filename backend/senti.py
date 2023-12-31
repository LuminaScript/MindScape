from textblob import TextBlob
import nltk
from googlesearch import Search

# Download the necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_sentiment(diary_text): 

    # # Sample diary text
    # diary_text = """
    # Dear diary,
    # Today was a day full of mixed emotions. I woke up feeling a bit gloomy, but later, the beautiful sunrise cheered me up. 
    # In the evening, I had a disagreement with my friend, which made me feel quite frustrated.
    # However, I found solace in a good book, and that brought me some peace and contentment.
    # """

    # Analyze the sentiment of the diary text
    blob = TextBlob(diary_text)
    sentiment = blob.sentiment.polarity  # returns a value between -1 and 1

    # Define a wider range of adjectives for different sentiments
    adjectives = {
        'very_positive': ['ecstatic', 'delighted', 'elated'],
        'positive': ['happy', 'content', 'cheerful'],
        'neutral': ['ordinary', 'calm', 'average'],
        'negative': ['upset', 'frustrated', 'disappointed'],
        'very_negative': ['miserable', 'angry', 'despairing']
    }

    # Map sentiment scores to sentiment categories
    sentiment_categories = {
        'very_positive': (0.7, 1.0),
        'positive': (0.3, 0.7),
        'neutral': (-0.3, 0.3),
        'negative': (-0.7, -0.3),
        'very_negative': (-1.0, -0.7)
    }

    # Define music recommendations for different sentiment categories
    music_recommendations = {
        'very_positive': 'Uptown Funk by Mark Ronson ft. Bruno Mars',
        'positive': 'Here Comes the Sun by The Beatles',
        'neutral': 'Weightless by Marconi Union',
        'negative': 'Fix You by Coldplay',
        'very_negative': 'Hurt by Johnny Cash'
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

