# Dictionary to store session data
session_store = {}

def get_session_data(session_id):
    return session_store.get(session_id)

def set_session_data(session_id, data):
    session_store[session_id] = data