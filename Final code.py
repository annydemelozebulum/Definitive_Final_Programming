import random

# Hangman visuals according to guesses
hangman_graphics = [
    """
    ________
    |      |
    |      
    |      
    | | D E A D |     
    |
    """,
    """
    ________
    |      |
    |      O /
    |       
    |       
    | 
    """,
    """
    ________
    |      |
    |      O
    |     / 
    |       
    |
    """,
    """
    ________
    |      |
    |      O
    |     /| 
    |       
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |       
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |     / 
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |     / \\
    |
    """
]

# Word Dictionary with Categories
word_categories = {
    "Singers": ["adele", "drake", "rihanna", "beyonce", "eminem"],
    "TV Shows": ["friends", "lucifer", "riverdale", "euphoria", "vikings"],
    "Classmates": ["alberto", "guillermo", "natalia", "soraya", "timothy"]
}

# Possibilities of Messages depending on results: they are randomly chosen
possibilities_correct = ["Correct guess", "Great guess", "Good job", "Amazing Intuition", "You have nice techniques"]
possibilities_incorrect = ["Wrong attempt", "You're close, think a bit more", "Your hangman might die :("]

# Function for category and word selection
def choose_word(category):
    return random.choice(word_categories[category])

def choose_category():
    chosen_category = random.choice(list(word_categories.keys()))
    print("Category:", chosen_category)
    return chosen_category

# Function to display hangman graphic according to guesses
def display_hangman(guesses):
    print(hangman_graphics[6 - guesses])

# Function to check if the word is guessed
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Function for the main game
def play_hangman():
    while True:
        # Introduction
        print("Welcome to our Hangman Game!")
        name = input("Enter your name: ")
        print("Hello,", name ,"! Let's play Hangman.")

        # Choose a category and a word
        category = choose_category()
        word = choose_word(category)
        guessed_letters = []
        incorrect_guesses = 0

        # Game loop
        while incorrect_guesses < 6:
            # Display hangman graphic
            display_hangman(incorrect_guesses)

            # Display word with guessed letters
            display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
            print(display)

            # Player guess
            guess = input("Guess a letter: ").lower()

            # Checking if the guessed letter is correct
            if guess in word:
                correct_message = random.choice(possibilities_correct)
                print(correct_message, name, "!")
                guessed_letters.append(guess)
            else:
                incorrect_message = random.choice(possibilities_incorrect)
                print(incorrect_message, name, "!")
                incorrect_guesses += 1

            # Checking if the word is guessed
            if is_word_guessed(word, guessed_letters):
                print(f"Congratulations", name, " You guessed the word:" , word,"!")
                break

        else:
            print("Sorry, you ran out of lives. The word was:", word)
            print(hangman_graphics[0])

        # Restart Option at the end
        restart = input("Do you wish to restart? (yes/no): ").lower()
        if restart != "yes":
            print("Thanks for playing!")
            break

play_hangman()
