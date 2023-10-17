print("Welcome to my computer quiz")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
    
print("Okay! Lets play")
score = 0

answer_1 = input("What does CPU stand for? ").lower()
if answer_1 ==  "central processing unit":
    print("You got it right")
    score += 1
else:
    print("bubu")
    
answer_2 = input("What is the capital city of Japan? ").title()
if answer_2 ==  "Tokyo":
    print("You got it right")
    score += 1
else:
    print("bubu")
    
answer_3 = input("What is the capital of Australia? ").title()
if answer_3 ==  "Sydney":
    print("You got it right")
    score += 1
else:
    print("bubu")

print("Your total score is:" , score)
percentage = ((score/3) *100)
rounded_percentage = round(percentage)
print("Percentage: ", rounded_percentage, "%")

    
    