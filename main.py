# placement_chatbot_app/main.py
import streamlit as st
from auth.login import show_login
from auth.signup import show_signup
from pages.user_page import show_user_page
from pages.admin_page import show_admin_page
from db.database import init_db

st.set_page_config(page_title="IT Placement Chatbot", layout="centered")
init_db()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = ""
    st.session_state.username = ""

if st.session_state.logged_in:
    if st.session_state.role == "user":
        show_user_page()
    elif st.session_state.role == "admin":
        show_admin_page()
else:
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    with tab1:
        show_login()
    with tab2:
        show_signup()
