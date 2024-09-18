import json
import random

# Schema for each question in questions.json:
# {
#     "question": "The text of the question",
#     "options": ["Option A", "Option B", "Option C", "Option D"],
#     "correct_answer": "The correct option (e.g., 'Option A')"
# }

def load_questions():
    with open('alpha/questions.json', 'r') as file:
        return json.load(file)

def run_quiz(questions):
    print("\n========================================\n   Welcome to the Alpha-Quiz Master!\n========================================\nGet ready to challenge your knowledge across\nvarious topics. Each question brings you one\nstep closer to becoming a Quiz Champion!\nGood luck and may the facts be with you!\n")

    while True:
        try:
            quiz_length = int(input("How many questions would you like in the quiz? "))
            if 1 <= quiz_length <= len(questions):
                break
            else:
                print(f"Please enter a number between 1 and {len(questions)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    score = 0
    questions_answered = 0

    for question in random.sample(questions, quiz_length):
        print(question['question'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")
        
        while True:
            user_answer = input("Enter the number of your answer (or 'leave' to end the quiz): ").lower()
            
            if user_answer == 'leave':
                print(f"Quiz ended early. Your final score: {score}/{questions_answered}")
                return
            
            try:
                answer_index = int(user_answer) - 1
                if 0 <= answer_index < len(question['options']):
                    break
                else:
                    print("Invalid input. Please enter a number corresponding to the options.")
            except ValueError:
                print("Invalid input. Please enter a number or 'leave'.")
        
        questions_answered += 1
        if question['options'][answer_index] == question['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {question['correct_answer']}")
        
        print(f"Current score: {score}/{questions_answered}")
        print()  # Empty line for readability

    print(f"Quiz finished! Your final score: {score}/{quiz_length}")

if __name__ == "__main__":
    quiz_questions = load_questions()
    run_quiz(quiz_questions)
