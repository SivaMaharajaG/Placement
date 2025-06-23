# placement_chatbot_app/pages/user_page.py
import streamlit as st
from genai.prompt import handle_query
import sqlite3

def show_user_page():
    st.title("Placement Chatbot - User")
    st.write(f"Welcome {st.session_state.username}!")
    query = st.text_input("Ask about IT placements in Tamil Nadu by qualification")

    if st.button("Submit"):
        response = handle_query(query, st.session_state.username)
        st.write("### Response:")
        st.write(response)

        conn = sqlite3.connect("data/chat_history.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS history (username TEXT, question TEXT, answer TEXT)")
        c.execute("INSERT INTO history VALUES (?, ?, ?)", (st.session_state.username, query, response))
        conn.commit()
        conn.close()

    st.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))
