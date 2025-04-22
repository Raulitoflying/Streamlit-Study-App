"""
Quiz Box component for the Online Quiz Study App.

This module contains functions to render the quiz UI.
"""
import streamlit as st
from utils.helpers import check_answer, next_quiz_question

def render_quiz_question(current_question):
    """
    Render a quiz question with multiple choice options.
    
    Args:
        current_question: The current quiz question data
    """
    # Display question header
    st.markdown(f"### Question {st.session_state.current_quiz_index + 1} of {len(st.session_state.active_quiz_questions)}")
    
    # Display question directly on page with padding
    # Using question-section class which has proper styling for both light and dark modes
    st.markdown(f"<div class='question-section'><span class='question-text'>{current_question['question']}</span></div>", unsafe_allow_html=True)
    
    # Display options as radio buttons
    if not st.session_state.answer_selected:
        selected_option = st.radio(
            "Choose your answer:",
            current_question['options'],
            key=f"quiz_option_{st.session_state.current_quiz_index}"
        )
        
        # Center the submit button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Submit Answer", key="submit_answer_button", use_container_width=True):
                is_correct = check_answer(selected_option, current_question['correct_answer'])
                if is_correct:
                    st.success("Correct! 🎉")
                else:
                    st.error(f"Incorrect. The correct answer is: {current_question['correct_answer']}")
    else:
        # After answer is selected, show Next Question button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Next Question", key="next_quiz_button", use_container_width=True):
                next_quiz_question()
                st.rerun()

def render_progress_bar(current_index, total_cards, completed_cards):
    """
    Render a progress bar and indicator.
    
    Args:
        current_index: Index of current card
        total_cards: Total number of cards
        completed_cards: Number of completed cards
    """
    progress = completed_cards / total_cards
    st.progress(progress)
    st.markdown(f'<div class="progress-text">Question {current_index + 1} of {total_cards} • {completed_cards} completed ({int(progress * 100)}%)</div>', unsafe_allow_html=True)

def render_quiz_progress(current_index, total_questions, quiz_score):
    """
    Render progress for quiz mode.
    
    Args:
        current_index: Index of current question
        total_questions: Total number of questions
        quiz_score: Current quiz score
    """
    progress = current_index / total_questions
    st.progress(progress)
    st.markdown(f'<div class="progress-text">Question {current_index + 1} of {total_questions} • Score: {quiz_score}/{total_questions} ({int(progress * 100)}%)</div>', unsafe_allow_html=True)

def render_quote(quote):
    """
    Render a quote in italics at the bottom of the page.
    
    Args:
        quote: Quote text to display
    """
    st.markdown(f'<div class="quote">"{quote}"</div>', unsafe_allow_html=True)

def render_footer():
    """Render the app footer."""
    st.markdown('<div class="footer">Online Quiz Study App © 2025</div>', unsafe_allow_html=True)