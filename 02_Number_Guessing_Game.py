import random

first_digit = input("Enter a digit: ")

if first_digit.isdigit():
    first_digit = int(first_digit) 
    
    if first_digit <= 0:
        print("Please type in a number greater than 0.")
        quit()
        
else:
    print("Type in a digit.")
    quit()


random_number = random.randint(0, first_digit)
print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the number:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Type a number next time:")
        continue
    
    if user_guess == random_number:
        print("You got it right.")
        break
    elif user_guess > random_number:
            print("You are above the number")
    else:
        print("You are below the number.")
        
    print("You got it in", guesses, "guesses.")
             
    

        