"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Vašíček
email: filda.vasicek@gmail.com
discord: vasicekf
"""
import random
import time

def generate_secret_number():
    while True:
        number = str(random.randint(1000, 9999))
        if len(set(number)) == 4:
            return number

def get_user_guess():
    while True:
        guess = input("Enter a number: ").strip()
        if len(guess) != 4 or not guess.isdigit() or guess[0] == '0' or len(set(guess)) < 4:
            print("Invalid input! Make sure it's a 4-digit number with unique digits and doesn't start with 0.")
        else:
            return guess

def evaluate_guess(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = len(set(secret) & set(guess)) - bulls
    return bulls, cows

def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()
    guesses = 0
    start_time = time.time()

    while True:
        guess = get_user_guess()
        guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            print(f"It took you {elapsed_time} seconds.")
            if guesses <= 5:
                print("That's amazing!")
            elif guesses <= 10:
                print("That's average.")
            else:
                print("Not so good...")
            break
        else:
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bull_word}, {cows} {cow_word}")

if __name__ == "__main__":
    main()