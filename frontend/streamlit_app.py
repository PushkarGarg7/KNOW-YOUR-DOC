# # # import streamlit as st
# # # import requests

# # # st.set_page_config(page_title="File Processing Application")

# # # # Initialize session state if not already set
# # # if 'page' not in st.session_state:
# # #     st.session_state.page = 'main'

# # # def show_main_page():
# # #     st.title('File Processing Application')

# # #     # Display choice buttons
# # #     st.markdown("<h2 style='text-align: center;'>Choose the type of file you want to work with:</h2>", unsafe_allow_html=True)
# # #     col1, col2 = st.columns(2)

# # #     with col1:
# # #         if st.button('Work with PDF'):
# # #             st.session_state.page = 'pdf'

# # #     with col2:
# # #         if st.button('Work with Excel'):
# # #             st.session_state.page = 'excel'

# # # def show_pdf_page():
# # #     st.subheader('PDF Summarizer')
# # #     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
# # #     if uploaded_file is not None:
# # #         # Display the uploaded file name
# # #         st.write("Uploaded File:", uploaded_file.name)

# # #         # Saving upload
# # #         with open(uploaded_file.name, "wb") as f:
# # #             f.write(uploaded_file.getbuffer())

# # #         # Button to send file to backend
# # #         if st.button('Summarize PDF'):
# # #             files = {'file': open(uploaded_file.name, 'rb')}
# # #             response = requests.post('http://localhost:5000/summarize', files=files)
# # #             if response.status_code == 200:
# # #                 summary = response.json().get('summary')
# # #                 st.write('Summary:', summary)
# # #             else:
# # #                 st.write("Failed to get summary:", response.status_code)

# # #     if st.button('Go Back'):
# # #         st.session_state.page = 'main'

# # # def show_excel_page():
# # #     st.subheader('Excel Processor')
# # #     uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])
# # #     if uploaded_file is not None:
# # #         # Display the uploaded file name
# # #         st.write("Uploaded File:", uploaded_file.name)

# # #         # Saving upload
# # #         with open(uploaded_file.name, "wb") as f:
# # #             f.write(uploaded_file.getbuffer())

# # #         # Button to process Excel file
# # #         if st.button('Process Excel'):
# # #             files = {'file': open(uploaded_file.name, 'rb')}
# # #             response = requests.post('http://localhost:5000/process_excel', files=files)
# # #             if response.status_code == 200:
# # #                 data = response.json().get('data')
# # #                 st.write('Processed Data:', data)
# # #             else:
# # #                 st.write("Failed to process Excel file:", response.status_code)

# # #     if st.button('Go Back'):
# # #         st.session_state.page = 'main'

# # # # Page navigation
# # # if st.session_state.page == 'main':
# # #     show_main_page()
# # # elif st.session_state.page == 'pdf':
# # #     show_pdf_page()
# # # elif st.session_state.page == 'excel':
# # #     show_excel_page()


# # import streamlit as st
# # import requests

# # st.set_page_config(page_title="File Processing Application")

# # # Initialize session state if not already set
# # if 'page' not in st.session_state:
# #     st.session_state.page = 'main'

# # if 'session_id' not in st.session_state:
# #     st.session_state.session_id = None

# # def show_main_page():
# #     st.title('File Processing Application')

# #     # Display choice buttons
# #     st.markdown("<h2 style='text-align: center;'>Choose the type of file you want to work with:</h2>", unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)

# #     with col1:
# #         if st.button('Work with PDF'):
# #             st.session_state.page = 'pdf'

# #     with col2:
# #         if st.button('Work with Excel'):
# #             st.session_state.page = 'excel'

# # def show_pdf_page():
# #     st.subheader('PDF Summarizer')
# #     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
# #     if uploaded_file is not None:
# #         # Display the uploaded file name
# #         st.write("Uploaded File:", uploaded_file.name)

# #         # Saving upload
# #         with open(uploaded_file.name, "wb") as f:
# #             f.write(uploaded_file.getbuffer())

# #         # Button to send file to backend
# #         if st.button('Summarize PDF'):
# #             files = {'file': open(uploaded_file.name, 'rb')}
# #             response = requests.post('http://localhost:5000/summarize', files=files)
# #             if response.status_code == 200:
# #                 summary = response.json().get('summary')
# #                 st.write('Summary:', summary)
# #             else:
# #                 st.write("Failed to get summary:", response.status_code)

# #     if st.button('Go Back'):
# #         st.session_state.page = 'main'

# # def show_excel_page():
# #     st.subheader('Excel Processor')
# #     uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])
# #     if uploaded_file is not None:
# #         # Display the uploaded file name
# #         st.write("Uploaded File:", uploaded_file.name)

# #         # Saving upload
# #         with open(uploaded_file.name, "wb") as f:
# #             f.write(uploaded_file.getbuffer())

# #         # Button to process Excel file
# #         if st.button('Process Excel'):
# #             files = {'file': open(uploaded_file.name, 'rb')}
# #             response = requests.post('http://localhost:5000/process_excel', files=files)
# #             if response.status_code == 200:
# #                 data = response.json().get('data')
# #                 st.write('Processed Data:', data)
# #             else:
# #                 st.write("Failed to process Excel file:", response.status_code)

# #     if st.button('Go Back'):
# #         st.session_state.page = 'main'

# # def show_talk_to_file_page():
# #     st.subheader('Talk to Your File')
# #     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
# #     if uploaded_file is not None:
# #         # Display the uploaded file name
# #         st.write("Uploaded File:", uploaded_file.name)
        
# #         # Save the uploaded file
# #         with open(uploaded_file.name, "wb") as f:
# #             f.write(uploaded_file.getbuffer())
        
# #         if st.session_state.session_id is None:
# #             st.session_state.session_id = str(uuid.uuid4())
        
# #         # Display chat-like interface
# #         if 'chat_history' not in st.session_state:
# #             st.session_state.chat_history = []
        
# #         question = st.text_input("Enter your question:")
# #         if st.button('Ask'):
# #             files = {'file': open(uploaded_file.name, 'rb')}
# #             data = {'question': question, 'session_id': st.session_state.session_id}
# #             response = requests.post('http://localhost:5000/qa', files=files, data=data)
# #             if response.status_code == 200:
# #                 answer = response.json().get('answer')
# #                 st.session_state.chat_history.append({"question": question, "answer": answer})
# #             else:
# #                 st.write("Failed to get answer:", response.status_code)
        
# #         # Display chat history
# #         for chat in st.session_state.chat_history:
# #             st.write(f"**Question:** {chat['question']}")
# #             st.write(f"**Answer:** {chat['answer']}")
    
# #     if st.button('Go Back'):
# #         st.session_state.page = 'main'

# # # Page navigation
# # if st.session_state.page == 'main':
# #     show_main_page()
# # elif st.session_state.page == 'pdf':
# #     show_pdf_page()
# # elif st.session_state.page == 'excel':
# #     show_excel_page()
# # elif st.session_state.page == 'talk_to_file':
# #     show_talk_to_file_page()

# import streamlit as st
# import requests
# import uuid

# st.set_page_config(page_title="File Processing Application")

# # Initialize session state if not already set
# if 'page' not in st.session_state:
#     st.session_state.page = 'main'

# if 'session_id' not in st.session_state:
#     st.session_state.session_id = str(uuid.uuid4())

# def show_main_page():
#     st.title('File Processing Application')

#     # Display choice buttons
#     st.markdown("<h2 style='text-align: center;'>Choose the type of file you want to work with:</h2>", unsafe_allow_html=True)
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button('Work with PDF'):
#             st.session_state.page = 'pdf'

#     with col2:
#         if st.button('Work with Excel'):
#             st.session_state.page = 'excel'

# def show_pdf_page():
#     st.subheader('PDF Summarizer or Q&A')
#     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
#     if uploaded_file is not None:
#         # Display the uploaded file name
#         st.write("Uploaded File:", uploaded_file.name)

#         # Saving upload
#         with open(uploaded_file.name, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         # Button to send file to backend for summarization
#         if st.button('Summarize PDF'):
#             files = {'file': open(uploaded_file.name, 'rb')}
#             response = requests.post('http://localhost:5000/summarize', files=files)
#             if response.status_code == 200:
#                 summary = response.json().get('summary')
#                 st.write('Summary:', summary)
#             else:
#                 st.write("Failed to get summary:", response.status_code)

#         # Chat-like interface for Q&A
#         st.subheader('Talk to Your File')
#         if 'chat_history' not in st.session_state:
#             st.session_state.chat_history = []

#         question = st.text_input("Enter your question:")
#         if st.button('Ask'):
#             files = {'file': open(uploaded_file.name, 'rb')}
#             data = {'question': question, 'session_id': st.session_state.session_id}
#             response = requests.post('http://localhost:5000/qa', files=files, data=data)
#             if response.status_code == 200:
#                 answer = response.json().get('answer')
#                 st.session_state.chat_history.append({"question": question, "answer": answer})
#             else:
#                 st.write("Failed to get answer:", response.status_code)

#         # Display chat history
#         for chat in st.session_state.chat_history:
#             st.write(f"**Question:** {chat['question']}")
#             st.write(f"**Answer:** {chat['answer']}")

#     if st.button('Go Back'):
#         st.session_state.page = 'main'

# def show_excel_page():
#     st.subheader('Excel Processor')
#     uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])
#     if uploaded_file is not None:
#         # Display the uploaded file name
#         st.write("Uploaded File:", uploaded_file.name)

#         # Saving upload
#         with open(uploaded_file.name, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         # Button to process Excel file
#         if st.button('Process Excel'):
#             files = {'file': open(uploaded_file.name, 'rb')}
#             response = requests.post('http://localhost:5000/process_excel', files=files)
#             if response.status_code == 200:
#                 data = response.json().get('data')
#                 st.write('Processed Data:', data)
#             else:
#                 st.write("Failed to process Excel file:", response.status_code)

#     if st.button('Go Back'):
#         st.session_state.page = 'main'

# # Page navigation
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

def show_main_page():
    st.title('File Processing Application')

    # Display choice buttons
    st.markdown("<h2 style='text-align: center;'>Choose the type of file you want to work with:</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Work with PDF'):
            st.session_state.page = 'pdf'
            st.experimental_rerun()  # Rerun the app to reflect the state change

    with col2:
        if st.button('Work with Excel'):
            st.session_state.page = 'excel'
            st.experimental_rerun()  # Rerun the app to reflect the state change

def show_pdf_page():
    st.subheader('PDF Summarizer or Q&A')
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        # Display the uploaded file name
        st.write("Uploaded File:", uploaded_file.name)

        # Saving upload
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Button to send file to backend for summarization
        if st.button('Summarize PDF'):
            files = {'file': open(uploaded_file.name, 'rb')}
            response = requests.post('http://localhost:5000/summarize', files=files)
            if response.status_code == 200:
                summary = response.json().get('summary')
                st.write('Summary:', summary)
            else:
                st.write("Failed to get summary:", response.status_code)

        # Chat-like interface for Q&A
        st.subheader('Talk to Your File')
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        question = st.text_input("Enter your question:")
        if st.button('Ask'):
            files = {'file': open(uploaded_file.name, 'rb')}
            data = {'question': question, 'session_id': st.session_state.session_id}
            response = requests.post('http://localhost:5000/qa', files=files, data=data)
            if response.status_code == 200:
                answer = response.json().get('answer')
                st.session_state.chat_history.append({"question": question, "answer": answer})
            else:
                st.write("Failed to get answer:", response.status_code)

        # Display chat history
        for chat in st.session_state.chat_history:
            st.write(f"**Question:** {chat['question']}")
            st.write(f"**Answer:** {chat['answer']}")

    if st.button('Go Back'):
        st.session_state.page = 'main'
        st.experimental_rerun()  # Rerun the app to reflect the state change

def show_excel_page():
    st.subheader('Excel Processor')
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])
    if uploaded_file is not None:
        # Display the uploaded file name
        st.write("Uploaded File:", uploaded_file.name)

        # Saving upload
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Button to process Excel file
        if st.button('Process Excel'):
            files = {'file': open(uploaded_file.name, 'rb')}
            response = requests.post('http://localhost:5000/process_excel', files=files)
            if response.status_code == 200:
                data = response.json().get('data')
                st.write('Processed Data:', data)
            else:
                st.write("Failed to process Excel file:", response.status_code)

    if st.button('Go Back'):
        st.session_state.page = 'main'
        st.experimental_rerun()  # Rerun the app to reflect the state change

# Page navigation
if st.session_state.page == 'main':
    show_main_page()
elif st.session_state.page == 'pdf':
    show_pdf_page()
elif st.session_state.page == 'excel':
    show_excel_page()
