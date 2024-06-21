import os
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from backend.services.summary_service import summarize_pdf  # Adjust the import as needed
from backend.services.q_a import q_a  # Import your q_a service

app = Flask(__name__)

# Define the path to the database folder
app.config['database'] = os.path.join(os.getcwd(), 'backend', 'database')
app.config['pdf_folder'] = os.path.join(app.config['database'], 'pdf')

# Ensure the database and pdf directories exist
os.makedirs(app.config['pdf_folder'], exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/summarize', methods=['POST'])
def summarize():
    app.logger.debug("Request received")
    if 'file' not in request.files:
        app.logger.debug("No file part in the request")
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    app.logger.debug(f"File received: {file.filename}")
    if file.filename == '':
        app.logger.debug("No selected file")
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)  # Ensure the filename is secure
        file_path = os.path.join(app.config['pdf_folder'], filename)
        file.save(file_path)  # Save the file to the desired folder
        app.logger.debug(f"File saved to: {file_path}")

        # Summarize the PDF
        summary = summarize_pdf(file_path)
        app.logger.debug(f"Summary generated: {summary}")

        return jsonify({'message': 'File uploaded successfully', 'path': file_path, 'summary': summary})

@app.route('/qa', methods=['POST'])
def qa():
    app.logger.debug("Q&A Request received")
    if 'file' not in request.files or 'question' not in request.form or 'session_id' not in request.form:
        return jsonify({'error': 'File, question, and session_id are required'}), 400
    
    file = request.files['file']
    question = request.form['question']
    session_id = request.form['session_id']
    
    app.logger.debug(f"File received: {file.filename}")
    if file.filename == '':
        app.logger.debug("No selected file")
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['pdf_folder'], filename)
    file.save(file_path)
    app.logger.debug(f"File saved to: {file_path}")

    answer = q_a(file_path, question, session_id)
    app.logger.debug(f"Answer generated: {answer}")

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
