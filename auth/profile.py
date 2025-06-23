# placement_chatbot_app/auth/profile.py
import streamlit as st
import sqlite3

def show_profile():
    st.subheader("Edit Profile")
    username = st.session_state.username
    conn = sqlite3.connect("data/chat_history.db")
    c = conn.cursor()
    c.execute("SELECT password, qualification, role FROM users WHERE username=?", (username,))
    user = c.fetchone()

    new_password = st.text_input("New Password", type="password")
    new_qualification = st.text_input("New Qualification", value=user[1])
    new_role = st.selectbox("New Role", ["user", "admin"], index=["user", "admin"].index(user[2]))

    if st.button("Update Profile"):
        c.execute("UPDATE users SET password=?, qualification=?, role=? WHERE username=?",
                  (new_password or user[0], new_qualification, new_role, username))
        conn.commit()
        st.success("Profile updated successfully")
    conn.close()
