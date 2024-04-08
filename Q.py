questions = [
    {
        "question": "Which Pokémon Generaton is Claydol from?",
        "options": ["A: 1", "B: 3", "C: 4", "D: 6"],
        "answer": "B"
    },
    
    {
        "question": "Which Pokémon Generaton is Panpour from?",
        "options": ["A: 2", "B: 3", "C: 5", "D: 7"],
        "answer": "C"
    },

     {
        "question": "Which Pokémon Generaton is Yungoos from?",
        "options": ["A: 5", "B: 7", "C: 8", "D: 9"],
        "answer": "B"
    },
   {
        "question": "Which Pokémon Generaton is Wooper from?",
        "options": ["A: 2", "B: 3", "C: 4", "D: 7"],
        "answer": "A"
    },
 {
        "question": "Which Pokémon Generaton is Togepi from?",
        "options": ["A: 1", "B: 3", "C: 2", "D: 4"],
        "answer": "C"
    },
  {
        "question": "Which Pokémon Generaton is Grumpig from?",
        "options": ["A: 4", "B: 3", "C: 5", "D: 6"],
        "answer": "B"
    },
    {
        "question": "Which Pokémon Generaton is Deino from?",
        "options": ["A: 3", "B: 4", "C: 5", "D: 6"],
        "answer": "C"
    },
 {
        "question": "Which Pokémon Generaton is Scyther from?",
        "options": ["A: 1", "B: 2", "C: 4", "D: 3"],
        "answer": "A"
    },

{
        "question": "Which Pokémon eneraton is Klang from?",
        "options": ["A: 1", "B: 3", "C: 5", "D: 7"],
        "answer": "C"
    },

]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")
run_quiz(questions)
