
# import logging
# from flask import Flask, request, jsonify
# from io import BytesIO
# from backend.services.q_a import q_a
# from backend.services.summary_service import summarize_pdf

# app = Flask(__name__)

# logging.basicConfig(level=logging.DEBUG)

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

#     return jsonify({'answer': answer})

# if __name__ == '__main__':
#     app.run(debug=True)


import logging
from flask import Flask, request, jsonify
from io import BytesIO
from backend.services.q_a import q_a
from backend.services.summary_service import summarize_pdf
from backend.database.session_db import get_session_data  # Ensure this is imported


app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
