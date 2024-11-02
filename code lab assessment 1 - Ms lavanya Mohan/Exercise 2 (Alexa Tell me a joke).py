import random

def load_jokes(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def tell_joke(jokes):
    joke = random.choice(jokes)
    setup, punchline = joke.split("?", 1)
    print(f"Setup: {setup}?")
    input("Press Enter to see the punchline...")
    print(f"Punchline: {punchline}")

def main():
    # use the path to load the text
    jokes = load_jokes(r'C:\\Users\\ASUS\\Downloads\\code lab assessment 1 - Ms lavanya Mohan\\resources\\randomJokes.txt')
    
    print("Type 'alexa tell me a joke' to hear a joke or 'quit' to exit.")
    while True:
        command = input("Enter command: ")
        if command.lower() == "alexa tell me a joke":
            tell_joke(jokes)
        elif command.lower() == "quit":
            print("Thank you for listening! Goodbye!")
            break
        else:
            print("Sorry, I can't recognize the command. Please try again.")

if __name__ == "__main__":
    main()
