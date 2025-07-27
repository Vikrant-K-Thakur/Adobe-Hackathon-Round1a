from flask import Flask, request, jsonify
from extract_outline import extract_outline_from_pdf

app = Flask(__name__)

@app.route('/extract-outline', methods=['POST'])
def extract_outline():
    if 'pdf' not in request.files:
        return jsonify({"error": "No PDF file provided."}), 400
    file = request.files['pdf']
    if not file or not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Invalid file type. Please upload a PDF."}), 400
    try:
        output = extract_outline_from_pdf(file)
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": f"Failed to process PDF: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
