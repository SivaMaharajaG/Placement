# placement_chatbot_app/pages/history.py
import streamlit as st
import sqlite3

def show_history():
    st.subheader("Chat History")
    conn = sqlite3.connect("data/chat_history.db")
    c = conn.cursor()
    c.execute("SELECT question, answer FROM history WHERE username=?", (st.session_state.username,))
    rows = c.fetchall()
    for q, a in rows:
        st.markdown(f"**Q**: {q}\n\n**A**: {a}")
