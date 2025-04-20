"""
Quiz data module for the Online Quiz Study App.

This module contains the quiz data organized by categories.
"""

# Sample question data with categories (expanded to at least 10 per major subject)
flashcards = [
    # Math questions (10)
    {"question": "What is the formula for finding the area of a circle?", "answer": "A = πr²", "category": "Math"},
    {"question": "What is 7 × 8?", "answer": "56", "category": "Math"},
    {"question": "What is the Pythagorean theorem?", "answer": "a² + b² = c²", "category": "Math"},
    {"question": "What is the formula for the area of a triangle?", "answer": "A = (1/2) × base × height", "category": "Math"},
    {"question": "What is the square root of 144?", "answer": "12", "category": "Math"},
    {"question": "What is the formula for the volume of a sphere?", "answer": "V = (4/3) × π × r³", "category": "Math"},
    {"question": "What is the value of π (pi) to 2 decimal places?", "answer": "3.14", "category": "Math"},
    {"question": "What is the formula for the perimeter of a rectangle?", "answer": "P = 2(length + width)", "category": "Math"},
    {"question": "What does PEMDAS stand for?", "answer": "Parentheses, Exponents, Multiplication/Division, Addition/Subtraction", "category": "Math"},
    {"question": "What is 12³?", "answer": "1,728", "category": "Math"},

    # Science questions (10)
    {"question": "What is the largest planet in the solar system?", "answer": "Jupiter", "category": "Science"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au", "category": "Science"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100°C", "category": "Science"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein", "category": "Science"},
    {"question": "What is the chemical formula for water?", "answer": "H₂O", "category": "Science"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond", "category": "Science"},
    {"question": "What is the speed of light in a vacuum?", "answer": "299,792,458 meters per second", "category": "Science"},
    {"question": "What particle has a positive charge?", "answer": "Proton", "category": "Science"},
    {"question": "What is the process by which plants make their food?", "answer": "Photosynthesis", "category": "Science"},
    {"question": "What is the closest star to Earth?", "answer": "The Sun", "category": "Science"},

    # History questions (10)
    {"question": "In which year did World War II end?", "answer": "1945", "category": "History"},
    {"question": "What year was the Declaration of Independence signed?", "answer": "1776", "category": "History"},
    {"question": "Who was the first president of the United States?", "answer": "George Washington", "category": "History"},
    {"question": "What ancient civilization built the pyramids at Giza?", "answer": "Ancient Egyptians", "category": "History"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "answer": "Amelia Earhart", "category": "History"},
    {"question": "What was the name of the first artificial satellite launched into orbit?", "answer": "Sputnik 1", "category": "History"},
    {"question": "Which empire was ruled by Genghis Khan?", "answer": "Mongol Empire", "category": "History"},
    {"question": "In what year did the Berlin Wall fall?", "answer": "1989", "category": "History"},
    {"question": "Who wrote the 'I Have a Dream' speech?", "answer": "Martin Luther King Jr.", "category": "History"},
    {"question": "What event started World War I?", "answer": "The assassination of Archduke Franz Ferdinand", "category": "History"},

    # Geography questions
    {"question": "What is the capital of Canada?", "answer": "Ottawa", "category": "Geography"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo", "category": "Geography"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean", "category": "Geography"},
    {"question": "What is the longest river in the world?", "answer": "Nile River", "category": "Geography"},

    # Literature questions
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare", "category": "Literature"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell", "category": "Literature"},

    # Art questions
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci", "category": "Art"},
    {"question": "Who painted 'Starry Night'?", "answer": "Vincent van Gogh", "category": "Art"},
]

# Quiz mode questions (multiple choice format)
quiz_questions = [
    # Math quiz questions
    {
        "question": "What is 12 × 12?",
        "options": ["122", "144", "124", "142"],
        "correct_answer": "144",
        "category": "Math"
    },
    {
        "question": "What is the value of π (pi) rounded to 2 decimal places?",
        "options": ["3.14", "3.41", "3.16", "3.12"],
        "correct_answer": "3.14",
        "category": "Math"
    },
    {
        "question": "What is the square root of 81?",
        "options": ["8", "9", "10", "7"],
        "correct_answer": "9",
        "category": "Math"
    },
    {
        "question": "Which formula correctly represents the Pythagorean theorem?",
        "options": ["a² + b² = c²", "a + b = c", "a² - b² = c²", "a × b = c²"],
        "correct_answer": "a² + b² = c²",
        "category": "Math"
    },
    
    # Science quiz questions
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
        "category": "Science"
    },
    {
        "question": "What is the chemical symbol for oxygen?",
        "options": ["O", "Ox", "Og", "Om"],
        "correct_answer": "O",
        "category": "Science"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Liver", "Skin", "Lungs"],
        "correct_answer": "Skin",
        "category": "Science"
    },
    {
        "question": "Which of these is NOT a state of matter?",
        "options": ["Solid", "Liquid", "Gas", "Energy"],
        "correct_answer": "Energy",
        "category": "Science"
    },
    
    # History quiz questions
    {
        "question": "Who was the first president of the United States?",
        "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"],
        "correct_answer": "George Washington",
        "category": "History"
    },
    {
        "question": "In what year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "correct_answer": "1945",
        "category": "History"
    },
    {
        "question": "Which civilization built the Machu Picchu?",
        "options": ["Aztecs", "Mayans", "Incas", "Olmecs"],
        "correct_answer": "Incas",
        "category": "History"
    },
    {
        "question": "Who wrote the 'Communist Manifesto'?",
        "options": ["Vladimir Lenin", "Joseph Stalin", "Leon Trotsky", "Karl Marx"],
        "correct_answer": "Karl Marx",
        "category": "History"
    },
    
    # Geography quiz question
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": "Pacific Ocean",
        "category": "Geography"
    },
    
    # Art quiz question
    {
        "question": "Which of these is not a primary color?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "correct_answer": "Green",
        "category": "Art"
    }
]

# Inspirational quotes
quotes = [
    "Education is the passport to the future, for tomorrow belongs to those who prepare for it today. — Malcolm X",
    "The more that you read, the more things you will know. The more that you learn, the more places you'll go. — Dr. Seuss",
    "Learn as if you will live forever, live like you will die tomorrow. — Mahatma Gandhi",
    "Education is not the filling of a pail, but the lighting of a fire. — W.B. Yeats",
    "Knowledge is power. — Francis Bacon",
    "The beautiful thing about learning is that nobody can take it away from you. — B.B. King",
    "Live as if you were to die tomorrow. Learn as if you were to live forever. — Mahatma Gandhi",
    "The only person who is educated is the one who has learned how to learn and change. — Carl Rogers",
    "The mind is not a vessel to be filled, but a fire to be kindled. — Plutarch",
    "The cure for boredom is curiosity. There is no cure for curiosity. — Dorothy Parker"
]

def get_all_categories():
    """Extract and return all unique categories from questions."""
    return sorted(list(set([card["category"] for card in flashcards])))