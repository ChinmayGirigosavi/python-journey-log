guess = ""
guess_limit = 3
guess_count = 0
secret_guess = "chinmay"

while guess != secret_guess and guess_count <= guess_limit:
    guess = input("Enter the guess: ")
    guess_count += 1
    
if guess == secret_guess:
    print("Correct guess, you win!")
else:
    print("You ran out of limit, you lose!")