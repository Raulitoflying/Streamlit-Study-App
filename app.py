"""
Online Quiz Study App

A streamlit-based educational quiz application for interactive learning.
To run the app, use the following command in your terminal:
streamlit run app.py
"""

import streamlit as st

# Import modular components
from components.header import render_header
from components.sidebar import render_sidebar
from utils.helpers import initialize_session_state
from core import main

# Set page title and layout
st.set_page_config(
    page_title="Online Quiz Study App",
    layout="centered",
    initial_sidebar_state="expanded"
)

def run_app():
    """Main entry point for the Online Quiz Study App."""
    
    # Initialize session state variables
    initialize_session_state()
    
    # Render application header
    render_header()
    
    # Render sidebar and get selected options
    selected_category, num_cards = render_sidebar()
    
    # Store sidebar selections in session state for main.py to use
    st.session_state.selected_category = selected_category
    st.session_state.num_cards = num_cards
    
    # Render main content
    main.main()

if __name__ == "__main__":
    run_app()