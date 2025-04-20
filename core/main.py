"""
Main module for the Online Quiz Study App.

This module contains the main application logic.
"""

import streamlit as st
import random

# Import modules
from data.flashcards import flashcards, quiz_questions, quotes
from utils.helpers import (
    initialize_session_state, next_card, filter_by_category, 
    get_random_quote, apply_theme
)
from components.flashcard_box import (
    render_flashcard, render_quiz_question, render_progress_bar,
    render_quiz_progress, render_quote, render_footer
)

def main():
    """Main function to run the quiz application logic."""
    # Apply theme
    try:
        st.markdown(apply_theme(), unsafe_allow_html=True)
    except FileNotFoundError:
        # If CSS file isn't found, use inline CSS
        st.warning("Style file not found. Using default styling.")
    
    # Apply filters based on sidebar selections from app.py
    selected_category = st.session_state.get('selected_category', 'All Categories')
    num_cards = st.session_state.get('num_cards', len(flashcards))
    
    filtered_cards = filter_by_category(selected_category, flashcards)
    if len(filtered_cards) > num_cards:
        filtered_cards = filtered_cards[:num_cards]

    filtered_quiz_questions = filter_by_category(selected_category, quiz_questions)
    if len(filtered_quiz_questions) > num_cards:
        filtered_quiz_questions = filtered_quiz_questions[:num_cards]

    # Update active cards if filters changed
    if st.session_state.active_cards != filtered_cards:
        st.session_state.active_cards = filtered_cards
        st.session_state.current_card_index = 0
        st.session_state.cards_completed = 0

    # Update active quiz questions if filters changed
    if st.session_state.active_quiz_questions != filtered_quiz_questions:
        st.session_state.active_quiz_questions = filtered_quiz_questions
        st.session_state.current_quiz_index = 0

    # Main content based on mode
    if not st.session_state.quiz_mode:
        # Practice mode (formerly flashcard mode)
        if len(st.session_state.active_cards) > 0:
            # Render progress bar
            render_progress_bar(
                st.session_state.current_card_index,
                len(st.session_state.active_cards),
                st.session_state.cards_completed
            )
            
            # Display current question
            current_card = st.session_state.active_cards[st.session_state.current_card_index]
            render_flashcard(current_card)
        else:
            st.warning("No questions match your current filters. Please adjust your settings.")
    else:
        # Quiz mode
        if len(st.session_state.active_quiz_questions) > 0:
            # Render quiz progress
            render_quiz_progress(
                st.session_state.current_quiz_index,
                len(st.session_state.active_quiz_questions),
                st.session_state.quiz_score
            )
            
            # Display current quiz question
            current_question = st.session_state.active_quiz_questions[st.session_state.current_quiz_index]
            render_quiz_question(current_question)
        else:
            st.warning("No quiz questions match your current filters. Please adjust your settings.")

    # Quote of the day
    random_quote = get_random_quote(quotes)
    render_quote(random_quote)

    # Footer
    render_footer()

if __name__ == "__main__":
    # This block will not execute when imported
    st.set_page_config(
        page_title="Online Quiz Study App",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    initialize_session_state()
    main()