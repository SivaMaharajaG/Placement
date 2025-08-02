# placement_chatbot_app/auth/login.py
import streamlit as st
import sqlite3

def show_login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        conn = sqlite3.connect("data/chat_history.db")
        c = conn.cursor()
        c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        if result:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = result[0]
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
        conn.close()

