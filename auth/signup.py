# placement_chatbot_app/auth/signup.py
import streamlit as st
import sqlite3
from auth.login import show_login

def show_signup():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    qualification = st.selectbox("Qualification", ["B.Tech", "MCA", "B.Sc", "M.Sc"])
    role = st.selectbox("Role", ["user", "admin"])

    if st.button("Create Account"):
        if password != confirm:
            st.error("Passwords do not match")
            return
        conn = sqlite3.connect("data/chat_history.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, qualification TEXT, role TEXT)")
        try:
            c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, password, qualification, role))
            conn.commit()
            st.success("Account created. Please login.")
        except sqlite3.IntegrityError:
            st.error("Username already exists.")
        conn.close()
show_login()
