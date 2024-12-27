# THANOSNAPP Chemistry Quiz
def chemistry_quiz():
    print("Welcome to THANOSNAPP Chemistry Quiz!")
    score = 0
    questions = [
        {
            "question": "1. What is the chemical symbol for water?",
            "options": ["A) H2O", "B) O2", "C) CO2", "D) NaCl"],
            "answer": "A"
        },
        {
            "question": "2. What is the atomic number of Carbon?",
            "options": ["A) 6", "B) 8", "C) 12", "D) 14"],
            "answer": "A"
        },
        {
            "question": "3. Which gas is most abundant in Earth's atmosphere?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
            "answer": "C"
        },
        {
            "question": "4. What is the pH of pure water?",
            "options": ["A) 5", "B) 7", "C) 9", "D) 12"],
            "answer": "B"
        },
        {
            "question": "5. Which element is represented by the symbol 'Fe'?",
            "options": ["A) Lead", "B) Zinc", "C) Iron", "D) Fluorine"],
            "answer": "C"
        }
    ]
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
    print(f"\nQuiz completed! Your total score is: {score}/5")
chemistry_quiz()