from flask import Flask, request, jsonify
from pdf2image import convert_from_bytes
from PIL import Image, ImageOps
import base64
import io

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_png():
    try:
        # Get the base64 encoded PDF from the request
        data = request.json['pdf_base64']
        pdf_bytes = base64.b64decode(data)
        
        # Convert PDF to image(s)
        images = convert_from_bytes(pdf_bytes)
        
        # Convert the first page to PNG
        img = images[0]
        
        # Convert to grayscale and find the bounding box
        gray_image = ImageOps.grayscale(img)
        inverted_image = ImageOps.invert(gray_image)
        bbox = inverted_image.getbbox()
        
        # Crop the image to the bounding box
        if bbox:
            img = img.crop(bbox)
        
        # Encode the cropped image in base64
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'png_base64': img_base64})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
