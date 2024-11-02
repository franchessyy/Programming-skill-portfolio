import random

def display_menu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    choice = input("Select difficulty level (1-3): ")
    return choice

#this sets the difficulty of the quiz to easy, moderate. advanced
def random_int(difficulty):
    if difficulty == '1': 
        return random.randint(1, 9)
    elif difficulty == '2':  
        return random.randint(10, 99)
    elif difficulty == '3':  
        return random.randint(1000, 9999)

def decide_operation():
    return random.choice(['+', '-'])

def display_problem(difficulty):
    num1 = random_int(difficulty)
    num2 = random_int(difficulty)
    operation = decide_operation()
    question = f"{num1} {operation} {num2} ="
    return question, eval(f"{num1} {operation} {num2}")

def is_correct(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Good Job! your answer is Correct!")
        return 10  
    else:
        print("Oops! Incorrect! Try Again.")
        return 0  

def display_problem_with_attempts(difficulty):
    question, correct_answer = display_problem(difficulty)
    
    for attempt in range(2):  
        user_input = input(f"{question}  (answer or type 'exit' to quit) ")
        if user_input.lower() == 'exit':
            raise SystemExit  # Exits the program
        try:
            user_answer = int(user_input)
            score = is_correct(user_answer, correct_answer)
            if score > 0:
                return score  
            if attempt == 0: 
                print(f"The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
#displays the grade after quiz
    return 0  
def display_results(score):
    print(f"Your final score is {score}/100.")
    if score >= 100-89:
        print("Grade: A+")
    elif score >= 88-81:
        print("Grade: A")
    elif score >= 80-75:
        print("Grade: B")
    elif score >= 75-60:
        print("Grade: C")
    elif score >= 60-50:
        print("Grade: F")


def play_quiz():
    difficulty = display_menu()
    score = 0
    
    for _ in range(10): 
        score += display_problem_with_attempts(difficulty)
    
    display_results(score)

def main():
    while True:
        play_quiz()
        play_again = input("It was fun having you here! Woud you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing, hope to see you again soon! Goodbye!")
            break

if __name__ == "__main__":
    main()