from flask import Flask, request, send_file, jsonify
from wordcloud_graph import generate_wordcloud
import io

app = Flask(__name__)

@app.route('/generate_wordcloud', methods=['POST'])
def create_wordcloud():
    data = request.json
    print(data)  # Stampa data in console
    word_colors = data.get('wordColors', {})
    word_frequencies = data.get('wordFrequencies', {})
    default_color = data.get('default_color', '#000000')

    try:
        image_bytes = generate_wordcloud(word_colors, word_frequencies, default_color)
        return send_file(io.BytesIO(image_bytes), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)