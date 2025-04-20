"""
Helpers module for the Online Quiz Study App.

This module contains utility functions for the app.
"""

import random
import streamlit as st
from data.flashcards import flashcards, quiz_questions

def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    if 'current_card_index' not in st.session_state:
        st.session_state.current_card_index = 0
        
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False
        
    if 'active_cards' not in st.session_state:
        st.session_state.active_cards = flashcards.copy()
        
    if 'cards_completed' not in st.session_state:
        st.session_state.cards_completed = 0
        
    if 'quiz_mode' not in st.session_state:
        st.session_state.quiz_mode = False
        
    if 'current_quiz_index' not in st.session_state:
        st.session_state.current_quiz_index = 0
        
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
        
    if 'answer_selected' not in st.session_state:
        st.session_state.answer_selected = False
        
    if 'active_quiz_questions' not in st.session_state:
        st.session_state.active_quiz_questions = quiz_questions.copy()

def next_card():
    """Get next question and update session state."""
    if len(st.session_state.active_cards) > 0:
        st.session_state.cards_completed += 1
        if st.session_state.cards_completed >= len(st.session_state.active_cards):
            st.session_state.cards_completed = 0
            st.balloons()  # Celebration when all questions are completed
        
        # Get the next question index
        st.session_state.current_card_index = (st.session_state.current_card_index + 1) % len(st.session_state.active_cards)
    
    # Reset show_answer state
    st.session_state.show_answer = False

def toggle_answer():
    """Toggle visibility of the answer."""
    st.session_state.show_answer = not st.session_state.show_answer

def filter_by_category(category, cards):
    """Filter questions by category."""
    if category == "All Categories":
        return cards
    return [card for card in cards if card["category"] == category]

def shuffle_cards():
    """Shuffle the active questions."""
    random.shuffle(st.session_state.active_cards)
    st.session_state.current_card_index = 0
    st.session_state.cards_completed = 0
    st.session_state.show_answer = False

def check_answer(selected_option, correct_answer):
    """Check if the selected answer is correct."""
    st.session_state.answer_selected = True
    if selected_option == correct_answer:
        st.session_state.quiz_score += 1
        return True
    return False

def next_quiz_question():
    """Move to the next quiz question."""
    st.session_state.current_quiz_index = (st.session_state.current_quiz_index + 1) % len(st.session_state.active_quiz_questions)
    st.session_state.answer_selected = False

def toggle_quiz_mode():
    """Toggle between practice and quiz modes."""
    st.session_state.quiz_mode = not st.session_state.quiz_mode
    st.session_state.current_quiz_index = 0
    st.session_state.answer_selected = False
    st.session_state.quiz_score = 0

def reset_progress():
    """Reset all progress in the app."""
    st.session_state.cards_completed = 0
    st.session_state.current_card_index = 0
    st.session_state.show_answer = False
    st.session_state.quiz_score = 0
    st.session_state.current_quiz_index = 0
    st.session_state.answer_selected = False

def get_random_quote(quotes):
    """Return a random quote from the list of quotes."""
    return random.choice(quotes)

def load_css():
    """Load CSS from the style.css file."""
    with open('styles/style.css', 'r') as f:
        css = f.read()
    return css

def apply_theme():
    """Apply the theme by loading CSS."""
    css = load_css()
    return f"<style>{css}</style>"