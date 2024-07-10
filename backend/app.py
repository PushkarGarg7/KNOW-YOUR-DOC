

# import logging
# import os
# from flask import Flask, request, jsonify
# from io import BytesIO
# from backend.services.q_a import q_a
# from backend.services.summary_service import summarize_pdf
# from backend.database.session_db import get_session_data  # Ensure this is imported

# app = Flask(__name__)

# logging.basicConfig(level=logging.DEBUG)

# # Ensure the folder structure exists
# UPLOAD_FOLDER = os.path.join('database', 'files')
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/summarize', methods=['POST'])
# def summarize():
#     app.logger.debug("Request received")
#     if 'file' not in request.files:
#         app.logger.debug("No file part in the request")
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['file']
#     app.logger.debug(f"File received: {file.filename}")
#     if file.filename == '':
#         app.logger.debug("No selected file")
#         return jsonify({'error': 'No selected file'}), 400
#     if file:
#         file_content = BytesIO(file.read())
#         summary = summarize_pdf(file_content)
#         app.logger.debug(f"Summary generated: {summary}")
#         return jsonify({'message': 'File uploaded successfully', 'summary': summary})

# @app.route('/qa', methods=['POST'])
# def qa():
#     app.logger.debug("Q&A Request received")
#     if 'file' not in request.files or 'question' not in request.form or 'session_id' not in request.form:
#         return jsonify({'error': 'File, question, and session_id are required'}), 400
    
#     file = request.files['file']
#     question = request.form['question']
#     session_id = request.form['session_id']
    
#     app.logger.debug(f"File received: {file.filename}")
#     if file.filename == '':
#         app.logger.debug("No selected file")
#         return jsonify({'error': 'No selected file'}), 400

#     file_content = BytesIO(file.read())
#     answer = q_a(file_content, question, session_id)
#     app.logger.debug(f"Answer generated: {answer}")
#     app.logger.debug(f"Session ID: {session_id}")
#     app.logger.debug(f"Session Data: {get_session_data(session_id)}")

#     return jsonify({'answer': answer})

# @app.route('/process_excel', methods=['POST'])
# def process_excel():
#     app.logger.debug("Excel processing request received")
#     if 'file' not in request.files:
#         app.logger.debug("No file part in the request")
#         return jsonify({'error': 'No file part'}), 400
    
#     file = request.files['file']
#     if file.filename == '':
#         app.logger.debug("No selected file")
#         return jsonify({'error': 'No selected file'}), 400
    
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)
#     app.logger.debug(f"File saved to {file_path}")
    
#     # Simulate processing
#     data = {"message": f"File {file.filename} saved to {file_path}"}
#     return jsonify(data), 200

# if __name__ == '__main__':
#     app.run(debug=True)
import logging
import os
from flask import Flask, request, jsonify
from io import BytesIO
from backend.services.csv_qa import process_excel_for_qa
from backend.services.summary_service import summarize_pdf
from backend.database.session_db import get_session_data

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Ensure the folder structure exists
UPLOAD_FOLDER = os.path.join('database', 'files')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
        file_content = BytesIO(file.read())
        summary = summarize_pdf(file_content)
        app.logger.debug(f"Summary generated: {summary}")
        return jsonify({'message': 'File uploaded successfully', 'summary': summary})

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

    file_content = BytesIO(file.read())
    answer = q_a(file_content, question, session_id)
    app.logger.debug(f"Answer generated: {answer}")
    app.logger.debug(f"Session ID: {session_id}")
    app.logger.debug(f"Session Data: {get_session_data(session_id)}")

    return jsonify({'answer': answer})

@app.route('/process_excel', methods=['POST'])
def process_excel():
    app.logger.debug("Excel processing request received")
    if 'file' not in request.files:
        app.logger.debug("No file part in the request")
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        app.logger.debug("No selected file")
        return jsonify({'error': 'No selected file'}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    app.logger.debug(f"File saved to {file_path}")

    if 'query' not in request.form or 'session_id' not in request.form:
        return jsonify({'error': 'Query and session_id are required'}), 400

    query = request.form['query']
    session_id = request.form['session_id']

    response_text = process_excel_for_qa(file_path, query, session_id)
    
    return jsonify({'message': response_text}), 200

if __name__ == '__main__':
    app.run(debug=True)

