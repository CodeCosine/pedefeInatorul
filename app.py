from flask import Flask, request, jsonify
from pdf2image import convert_from_bytes
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_png():
    try:
        # Get the base64 encoded PDF from the request
        data = request.json['pdf_base64']
        print(data)
        pdf_bytes = base64.b64decode(data)
        
        # Convert PDF to image(s)
        images = convert_from_bytes(pdf_bytes)
        
        # Convert the first page to PNG and encode it in base64
        img = images[0]
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'png_base64': img_base64})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500