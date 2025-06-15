# API-Based Quiz Game using Python
This is an interactive Python Quiz Game that fetches real-time multiple-choice questions from the Open Trivia Database API. The user selects a preferred category and difficulty level, and the program dynamically loads questions from the internet. It's a great project to explore API integration, user input handling, and Python basics in a fun and practical way.

# Features
- Real-Time Questions: Questions are fetched live from the Open Trivia Database API.
- Category Selection: Choose from categories like Computer, Mathematics, Movies, and Sports.
- Difficulty Levels: Select between easy, medium, and hard levels.
-  Randomized Options: Answer options are shuffled to ensure fairness.
-  Real-time scoring with immediate feedback after each question.

# Technologies Used
- Python
- Libraries (random, requests)

#  How does it works?
- The program prompts the user to select: (Number of questions, Category, Difficulty level)
- It then sends a request to the Open Trivia Database API to fetch random quiz questions.
- For each question:
    - All answer options (correct + incorrect) are combined and shuffled.
    - The user types the exact answer as displayed.
    - The program validates the answer, updates the score, and gives instant feedback.
    - At the end, the final score is displayed.

# Notes
- Ensure you have a stable internet connection, as the quiz pulls questions live from an online API.
- Answers must be typed exactly as displayed (only disadvantage)

# Disclaimer
This project is unlicensed and made purely for educational purposes. You are free to explore, learn, and modify, but commercial use or redistribution is not intended.

