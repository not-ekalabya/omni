import google.generativeai as genai
import random

def load_api_key():
    api_key = "your_api_key_here"
    return api_key

def setup_genai():
    api_key = load_api_key()
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

def get_user_preferences():
    topics = input("Enter quiz topics (comma-separated) or 'default': ").lower()
    if topics == 'default':
        return ['general knowledge'], ['MCQ', 'Short Answer', 'One Word Answer'], 'Medium', 'Moderate', 'Friendly'
    
    topics = [topic.strip() for topic in topics.split(',')]
    
    question_types = input("Enter desired question types (MCQ, Short Answer, One Word Answer, comma-separated, 'all' for mixed, or 'default'): ").lower()
    if question_types == 'default':
        return topics, ['MCQ', 'Short Answer', 'One Word Answer'], 'Medium', 'Moderate', 'Friendly'
    elif question_types == 'all':
        types = ['MCQ', 'Short Answer', 'One Word Answer']
    else:
        types = [t.strip() for t in question_types.split(',')]
    
    difficulty = input("Enter question difficulty level (Easy, Medium, Hard) or 'default': ").strip().capitalize()
    if difficulty == 'Default':
        return topics, types, 'Medium', 'Moderate', 'Friendly'
    
    grading_strictness = input("Enter grading strictness (Lenient, Moderate, Strict) or 'default': ").strip().capitalize()
    if grading_strictness == 'Default':
        grading_strictness = 'Moderate'
    
    personality = input("Enter bot personality (e.g., Friendly, Sarcastic, Encouraging) or 'default': ").strip().capitalize()
    if personality == 'Default':
        personality = 'Friendly'
    
    return topics, types, difficulty, grading_strictness, personality

def generate_question_with_personality(model, topics, question_type, difficulty, personality):
    prompt = f"""As a {personality} quiz host, generate a {difficulty} {question_type} question about {', '.join(topics)}.
    Include a brief, personality-appropriate introduction before the question.
    For MCQ, include 4 options.
    Do not include the correct answer in your response."""
    response = model.generate_content(prompt)
    return response.text

def evaluate_answer_with_personality(model, question, user_answer, grading_strictness, personality):
    prompt = f"""As a {personality} quiz host, evaluate the user's answer to the following question with {grading_strictness} grading:

    Question:
    {question}

    User's answer: {user_answer}

    Respond with 'Correct' or 'Incorrect', followed by a brief, personality-appropriate comment."""
    response = model.generate_content(prompt)
    return response.text.strip()

def get_explanation_with_personality(model, question, personality):
    prompt = f"""As a {personality} quiz host, provide the correct answer and a brief explanation for the following question:

    {question}

    Include a personality-appropriate comment before giving the explanation."""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_welcome_message(model, personality):
    prompt = f"""As a {personality} quiz host, generate a brief welcome message for the start of a quiz.
    Keep it concise and engaging, reflecting the {personality} personality."""
    response = model.generate_content(prompt)
    return response.text.strip()

def run_quiz(model):
    print("Welcome to the customizable quiz!")
    print("You can enter 'default' at any prompt to use preset values for the remaining options.")
    topics, question_types, difficulty, grading_strictness, personality = get_user_preferences()
    
    while True:
        try:
            quiz_length = input("How many questions would you like in the quiz? (or 'default' for 10): ")
            if quiz_length.lower() == 'default':
                quiz_length = 10
                break
            quiz_length = int(quiz_length)
            if quiz_length > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'default'.")

    print(f"\nStarting quiz with {quiz_length} questions on {', '.join(topics)} at {difficulty} difficulty.")
    print(f"Question types: {', '.join(question_types)}")
    print(f"Grading strictness: {grading_strictness}")
    print(f"Bot personality: {personality}")
    
    welcome_message = generate_welcome_message(model, personality)
    print("\n" + welcome_message + "\n")
    
    print("Let's begin!\n")

    score = 0
    questions_answered = 0

    for question_num in range(1, quiz_length + 1):
        question_type = random.choice(question_types)
        print(f"\nQuestion {question_num}:")
        question = generate_question_with_personality(model, topics, question_type, difficulty, personality)
        print(question)
        
        user_answer = input("Enter your answer (or 'leave' to end the quiz): ")
        
        if user_answer.lower() == 'leave':
            print(f"Quiz ended early. Your final score: {score}/{questions_answered}")
            return
        
        questions_answered += 1
        evaluation = evaluate_answer_with_personality(model, question, user_answer, grading_strictness, personality)
        
        if "correct" in evaluation.lower():
            print(evaluation)
            score += 1
        else:
            print(evaluation)
            explanation = get_explanation_with_personality(model, question, personality)
            print("Here's the correct answer and explanation:")
            print(explanation)
        
        print(f"Current score: {score}/{questions_answered}")
        print()  # Empty line for readability

    print(f"Quiz finished! Your final score: {score}/{quiz_length}")

if __name__ == "__main__":
    model = setup_genai()
    run_quiz(model)