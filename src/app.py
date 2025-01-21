from flask import Flask, request, send_file, jsonify
from barre_graph import generate_barre_in_pila
from dispersione import generate_dispersione
from overaly_images import overlayimages
from pie3d_graph import generate_pie3d
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
    img_byte_arr = overlayimages(image1, image2)

    return send_file(img_byte_arr, mimetype='image/png')


@app.route('/generate_barre_in_pila', methods=['POST'])
def create_barre_in_pila():
    data = request.json
    print(data)
    colors = data.get('colors', [])
    labels = data.get('labels', [])
    sizes = data.get('sizes', [])

    try:
        image_bytes = generate_barre_in_pila(colors, labels, sizes)
        return send_file(io.BytesIO(image_bytes), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/generate_pie3d', methods=['POST'])
def create_pie3d():
    data = request.json
    print(data)
    colors = data.get('colors', [])
    labels = data.get('labels', [])
    sizes = data.get('sizes', [])
    explode = data.get('explode', [])
    title = data.get('title', '3D Pie Chart')

    try:
        image_bytes = generate_pie3d(colors, labels, sizes, explode, title)
        return send_file(io.BytesIO(image_bytes), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/dispersione', methods=['POST'])
def create_dispersione():
    data = request.json
    print(data)
    x = data.get('x', [])
    y = data.get('y', [])
    labels = data.get('labels', [])

    try:
        image_bytes = generate_dispersione(x, y, labels)
        return send_file(io.BytesIO(image_bytes), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)