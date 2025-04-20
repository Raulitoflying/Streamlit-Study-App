"""
Sidebar component for the Online Quiz Study App.

This module contains functions to render the sidebar controls.
"""
import streamlit as st
from utils.helpers import (
    toggle_quiz_mode, reset_progress, shuffle_cards
)
from data.flashcards import get_all_categories, flashcards

def render_sidebar():
    """
    Render the sidebar with all app controls.
    """
    with st.sidebar:
        st.markdown("## 🛠️ App Controls")
        
        # Category selection
        all_categories = get_all_categories()
        selected_category = st.selectbox(
            "Select Category:",
            ["All Categories"] + all_categories
        )
        
        # Number of questions to review
        num_cards = st.slider(
            "Number of Questions to Review:",
            min_value=1,
            max_value=len(flashcards),
            value=len(flashcards)
        )
        
        # Shuffle option
        if st.button("🔀 Shuffle Questions"):
            shuffle_cards()
        
        # Quiz mode toggle
        quiz_toggle = st.checkbox("Quiz Mode", value=st.session_state.quiz_mode)
        if quiz_toggle != st.session_state.quiz_mode:
            toggle_quiz_mode()
        
        # Reset progress
        if st.button("🔄 Reset Progress"):
            reset_progress()
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("This app helps you study with interactive quizzes. You can review questions and answers, or test yourself in quiz mode.")
        
        return selected_category, num_cards