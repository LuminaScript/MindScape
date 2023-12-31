from flask import Flask, render_template, request, jsonify
from templates.senti import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/get_music_links', methods=['POST'])
# def get_music_links():
#     data = request.get_json()
#     diary_text = data.get('diary_text', '')

#     # Perform sentiment analysis and get music links
#     print("diary text: ")
#     print(diary_text)
#     music_links = analyze_sentiment(diary_text)
#     print("music links fetched from google: ")
#     print(music_links)

#     response = {
#         'links': music_links
#     }
#     return jsonify(response)
@app.route('/get_music_links', methods=['POST'])
def get_music_links():
    data = request.get_json()
    diary_text = data.get('diary_text', '')

    # Perform sentiment analysis and get music links
    print("diary text: ")
    print(diary_text)
    music_links = analyze_sentiment(diary_text)
    print("music links fetched from google: ")
    print(music_links)

    response = {
        'links': music_links
    }
    print("response: ")
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
