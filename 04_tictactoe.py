
# Step 1 : Choose user input
while True:
    user_1 = input("Choose X or O:").upper()
    if user_1 == "X" or user_1 =="O":
        break
    else:
        print("Enter correct choice")

if user_1 == "X":
    user_2 = "O"
else:
    user_2 = "X"
        
print("User 1:", user_1, "User 2:", user_2)

# Step 2 : Create a board

board = []
for row in range(3):
    board.append([""] * 3)
    print(board[row])
     
# Ask user to make a move
inputrow = input("Please pick a row.")
inputcolumn = input("Please pick a column .")

def isValid(row, col):
    if not (row >= 0 and row < 3 and col >= 0 and col < 3):
        return False
    return board[row][col] == ""

print (isValid(int(inputrow), int(inputcolumn)))
 
