

# import streamlit as st
# import requests
# import uuid

# st.set_page_config(page_title="File Processing Application")

# # Initialize session state if not already set
# if 'page' not in st.session_state:
#     st.session_state.page = 'main'

# if 'session_id' not in st.session_state:
#     st.session_state.session_id = str(uuid.uuid4())

# def reset_session():
#     st.session_state.vectorstore = None
#     st.session_state.chat_history = []
#     st.session_state.session_id = str(uuid.uuid4())

# def show_main_page():
#     st.title('File Processing Application')

#     st.markdown("<h2 style='text-align: center;'>Choose the type of file you want to work with:</h2>", unsafe_allow_html=True)
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button('Work with PDF'):
#             st.session_state.page = 'pdf'
#             st.experimental_rerun()

#     with col2:
#         if st.button('Work with Excel'):
#             st.session_state.page = 'excel'
#             st.experimental_rerun()

# def show_pdf_page():
#     st.subheader('PDF Summarizer or Q&A')
#     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", key="pdf_uploader")

#     if uploaded_file is not None:
#         if 'uploaded_file' not in st.session_state or st.session_state.uploaded_file != uploaded_file.name:
#             reset_session()
#             st.session_state.uploaded_file = uploaded_file.name
#             st.write("New file uploaded, session reset.")

#         st.write("Uploaded File:", uploaded_file.name)

#         if st.button('Summarize PDF'):
#             files = {'file': uploaded_file}
#             response = requests.post('http://localhost:5000/summarize', files=files)
#             if response.status_code == 200:
#                 summary = response.json().get('summary')
#                 st.write('Summary:', summary)
#             else:
#                 st.write("Failed to get summary:", response.status_code)

#         st.subheader('Talk to Your File')
#         if 'chat_history' not in st.session_state:
#             st.session_state.chat_history = []

#         question = st.text_input("Enter your question:")
#         if st.button('Ask'):
#             files = {'file': uploaded_file}
#             data = {'question': question, 'session_id': st.session_state.session_id}
#             response = requests.post('http://localhost:5000/qa', files=files, data=data)
#             if response.status_code == 200:
#                 answer = response.json().get('answer')
#                 st.session_state.chat_history.append({"question": question, "answer": answer})
#             else:
#                 st.write("Failed to get answer:", response.status_code)

#         for chat in st.session_state.chat_history:
#             st.write(f"**Question:** {chat['question']}")
#             st.write(f"**Answer:** {chat['answer']}")

#     if st.button('Go Back'):
#         st.session_state.page = 'main'
#         st.experimental_rerun()

# def show_excel_page():
#     st.subheader('Excel Processor')
#     uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])
#     if uploaded_file is not None:
#         st.write("Uploaded File:", uploaded_file.name)

#         if st.button('Process Excel'):
#             files = {'file': uploaded_file}
#             response = requests.post('http://localhost:5000/process_excel', files=files)
#             if response.status_code == 200:
#                 data = response.json().get('data')
#                 st.write('Processed Data:', data)
#             else:
#                 st.write("Failed to process Excel file:", response.status_code)

#     if st.button('Go Back'):
#         st.session_state.page = 'main'
#         st.experimental_rerun()

# if st.session_state.page == 'main':
#     show_main_page()
# elif st.session_state.page == 'pdf':
#     show_pdf_page()
# elif st.session_state.page == 'excel':
#     show_excel_page()


import streamlit as st
import requests
import uuid

st.set_page_config(page_title="File Processing Application")

# Initialize session state if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'main'

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

def reset_session():
    st.session_state.vectorstore = None
    st.session_state.chat_history = []
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.uploaded_file = None

def show_main_page():
    st.title('File Processing Application')

    st.markdown("<h2 style='text-align: center;'>Choose the type of file you want to work with:</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Work with PDF'):
            st.session_state.page = 'pdf'
            st.experimental_rerun()

    with col2:
        if st.button('Work with Excel'):
            st.session_state.page = 'excel'
            st.experimental_rerun()

def show_pdf_page():
    st.subheader('PDF Summarizer or Q&A')
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", key="pdf_uploader")

    if uploaded_file is not None:
        if 'uploaded_file' not in st.session_state or st.session_state.uploaded_file != uploaded_file.name:
            reset_session()
            st.session_state.uploaded_file = uploaded_file.name
            st.write("New file uploaded, session reset.")

        st.write("Uploaded File:", uploaded_file.name)

        if st.button('Summarize PDF'):
            files = {'file': uploaded_file}
            response = requests.post('http://localhost:5000/summarize', files=files)
            if response.status_code == 200:
                summary = response.json().get('summary')
                st.write('Summary:', summary)
            else:
                st.write("Failed to get summary:", response.status_code)

        st.subheader('Talk to Your File')
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        question = st.text_input("Enter your question:")
        if st.button('Ask'):
            files = {'file': uploaded_file}
            data = {'question': question, 'session_id': st.session_state.session_id}
            response = requests.post('http://localhost:5000/qa', files=files, data=data)
            if response.status_code == 200:
                answer = response.json().get('answer')
                st.session_state.chat_history.append({"question": question, "answer": answer})
            else:
                st.write("Failed to get answer:", response.status_code)

        for chat in st.session_state.chat_history:
            st.write(f"**Question:** {chat['question']}")
            st.write(f"**Answer:** {chat['answer']}")

    if st.button('Go Back'):
        st.session_state.page = 'main'
        st.experimental_rerun()

def show_excel_page():
    st.subheader('Excel Processor')
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])
    if uploaded_file is not None:
        st.write("Uploaded File:", uploaded_file.name)

        if st.button('Process Excel'):
            files = {'file': uploaded_file}
            response = requests.post('http://localhost:5000/process_excel', files=files)
            if response.status_code == 200:
                data = response.json().get('data')
                st.write('Processed Data:', data)
            else:
                st.write("Failed to process Excel file:", response.status_code)

    if st.button('Go Back'):
        st.session_state.page = 'main'
        st.experimental_rerun()

if st.session_state.page == 'main':
    show_main_page()
elif st.session_state.page == 'pdf':
    show_pdf_page()
elif st.session_state.page == 'excel':
    show_excel_page()
