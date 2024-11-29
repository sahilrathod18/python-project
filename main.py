from quizgame import load_questions, display_question, get_user_answer, calculate_score

def main():
    print("Welcome to the Quiz Game!")

    questions = load_questions()
    user_answers = []

    for question in questions:
        display_question(question["question"], question["options"])
        user_answer = get_user_answer()
        user_answers.append(user_answer)

    score = calculate_score(user_answers, questions)
    print(f"\nYour score: {score}/{len(questions)}")

    if score == len(questions):
        print("Excellent! You're a quiz master! 🎉")
    elif score >= len(questions) // 2:
        print("Good job! Keep learning! 😊")
    else:
        print("Better luck next time! Keep practicing! 💪")

if __name__ == "__main__":
    main()
