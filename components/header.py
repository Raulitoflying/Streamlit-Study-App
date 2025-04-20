"""
Header component for the Online Quiz Study App.

This module contains functions to render the header section of the app.
"""
import streamlit as st

def render_header():
    """
    Render the app header with title, subtitle, and emoji.
    """
    st.markdown('<div class="main-header"><h1>🧠 Online Quiz Study App</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Practice any subject with interactive quizzes</div>', unsafe_allow_html=True)