import json

def load_questions(filename="questions.json"):
    """Loads quiz questions from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)

def display_question(question, options):
    """Displays a quiz question and its options."""
    print("\n" + question)
    for option in options:
        print(option)

def get_user_answer():
    """Prompts the user to input an answer."""
    return input("Enter your answer (A, B, C, or D): ").strip().upper()

def calculate_score(user_answers, questions):
    """Calculates the user's score based on their answers."""
    score = 0
    for user_answer, question in zip(user_answers, questions):
        if user_answer == question["answer"]:
            score += 1
    return score
