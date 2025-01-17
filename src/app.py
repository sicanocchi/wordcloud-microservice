from flask import Flask, request, send_file, jsonify
from wordcloud_graph import generate_wordcloud
import io
from PIL import Image

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
    

@app.route('/overlay_images', methods=['POST'])
def overlay_images():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({'error': 'Both image1 and image2 are required'}), 400

    image1 = Image.open(request.files['image1'])
    image2 = Image.open(request.files['image2'])

    # Ensure both images have the same size
    image2 = image2.resize(image1.size)

    # Overlay images
    combined_image = Image.alpha_composite(image1.convert('RGBA'), image2.convert('RGBA'))

    # Save to a bytes buffer
    img_byte_arr = io.BytesIO()
    combined_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return send_file(img_byte_arr, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)