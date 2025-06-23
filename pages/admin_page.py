# placement_chatbot_app/pages/admin_page.py
import streamlit as st
import sqlite3

def show_admin_page():
    st.title("Admin Page")
    conn = sqlite3.connect("data/chat_history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history")
    rows = c.fetchall()

    st.subheader("Chat History")
    for row in rows:
        st.markdown(f"**User**: {row[0]}\n\n**Q**: {row[1]}\n\n**A**: {row[2]}")
    conn.close()
    st.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))
