"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
"""Use 'pow' to call the power function with other tokens"""

# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)

# while exit_condition_not_reached:

while True:
    # ask user what they would like to calculate
    user_input = (input("What would you like to calculate?: "))
    # creating a variable token that takes the user input and creates a tokenized list
    token_input = user_input.split(" ")
    
    # if user presses q, exit calculator 
    if "q" in token_input:
        print("Exit")
        break

    # make it so user_input must be greater than two numbers 
    elif len(token_input) < 2:
        print("You have to input more than two numbers!")
        continue

    # create variables for operating functions and our first number input
    operator = token_input[0]
    num1 = token_input[1]

    # create if statements for num 2 and num 3 
    if len(token_input) < 3:
        num2 = "0"
    else:
        num2 = token_input[2]
    
    if len(token_input) > 3:
        num3 = token_input[3]

    # if user enter add, we call the add function, and repeat for other calculations
    # ex: + 2 3 
    if token_input[0] == "+":
        sum = add(int(token_input[1]), int(token_input[2]))
        print(sum)

    # if user wants to subract, we call the sub function and repeat for other calculations
    # ex - 2 3 
   
    if token_input[0] == "-":
        
        s = subtract(int(token_input[1]), int(token_input[2]))
        print(s)
        


    


#     input = consume_input()
#     output = evaluate_input(input)
#     print(output)