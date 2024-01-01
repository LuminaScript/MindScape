from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import nltk
from googlesearch import Search
from flask_cors import CORS 
import openai

app = Flask(__name__)
CORS(app)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Download the necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

music_links_data = list()

openai.api_key = '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'
def generate_image_from_story(story):
    try:
        response = openai.Image.create(
            prompt=story,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/generate_image', methods=['POST'])
def handle_generate_image():
    data = request.json
    story = data.get('story', '')
    if not story:
        return jsonify({"error": "Story content is required"}), 400
    image_url = generate_image_from_story(story)
    return jsonify({"image_url": image_url})


def generate_short_story(noun1, noun2, noun3):
    prompt = f"Write a short story about {noun1}, {noun2}, and {noun3}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

@app.route('/generate_story', methods=['POST'])
def handle_generate_story():
    data = request.json
    nouns = data.get('nouns', [])
    if len(nouns) != 3:
        return jsonify({"error": "Exactly three nouns are required"}), 400
    story = generate_short_story(*nouns)
    return jsonify({"story": story})

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/diary')
def diary():
    return render_template("diary.html")

@app.route('/sandtable')
def sandtable():
    return render_template("sandtable.html")

@app.route('/sandtableart')
def sandtableart():
    return render_template("sandtableart.html")

@app.route('/metachar')
def metachar():
    return render_template("metachar.html")

@app.route('/get_music_links', methods=['POST'])
def get_music_links():
    try:
        data = request.get_json()
        diary_text = data.get('diary_text')

        # Call the analyze_sentiment function and get the music links
        playable_music_links = analyze_sentiment(diary_text)

        return jsonify(playable_music_links)
    except Exception as e:
        return jsonify({'error': str(e)})


def analyze_sentiment(diary_text):
    # Analyze the sentiment of the diary text
    blob = TextBlob(diary_text)
    sentiment = blob.sentiment.polarity  # returns a value between -1 and 1

    # Define a wider range of adjectives for different sentiments
    adjectives = {
        'extremely_positive': ['ecstatic', 'delighted', 'elated'],
        'very_positive': ['happy', 'content', 'cheerful'],
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
        'extremely_positive': (0.7, 1.0),
        'very_positive': (0.5, 0.7),
        'quite_happy': (0.3, 0.5),
        'mildly_happy': (0.1, 0.3),
        'neutral': (-0.1, 0.1),
        'mildly_negative': (-0.3, -0.1),
        'negative': (-0.5, -0.3),
        'quite_negative': (-0.7, -0.5),
        'very_negative': (-0.9, -0.7),
        'extremely_negative': (-1.0, -0.9)
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
if __name__ == '__main__':
    app.run(debug=True)
