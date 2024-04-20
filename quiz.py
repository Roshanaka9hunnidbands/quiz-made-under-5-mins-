# Define a list of questions, answers, and options
questions = [
    "What is the capital of France?",
    "Which continent is the largest by land area?",
    "What is the longest river in the world?",
    "Which country is famous for kangaroos and koalas?"
]

options = [
    ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
    ["A. Asia", "B. Europe", "C. Africa", "D. North America"],
    ["A. Nile", "B. Amazon", "C. Mississippi", "D. Yangtze"],
    ["A. Brazil", "B. Australia", "C. Canada", "D. South Africa"]
]

answers = ["B", "A", "A", "B"]  # Corrected answer for the longest river question

# Define a function to run the quiz
def run_quiz(questions, options, answers):
    score = 0
    for i in range(len(questions)):
        print("Question", i + 1, ":", questions[i])
        for option in options[i]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answers[i])
        print()
    
    print("Quiz completed! You got", score, "out of", len(questions), "questions correct.")

# Run the quiz
run_quiz(questions, options, answers)
