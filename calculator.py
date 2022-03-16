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
        print("You have to input more than two inputs!")
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

    result = None

    # make sure our user is inputting actual numbers!
    if not num1.isdigit() or not num2.isdigit():
        print("Sorry! You have to enter numbers!")
        continue

    # if user enter add, we call the add function, and repeat for other calculations
    # ex: + 2 3 
    elif operator == "+":
        result = add(float(num1), float(num2))

    # add subtraction opperator 
    elif operator == "-":
        result = subtract(float(num1), float(num2))
    
    # add multiplication operator
    elif operator == "*":
        result = multiply(float(num1), float(num2))




    print(result) 
        

    # if user wants to subract, we call the sub function and repeat for other calculations
    # ex - 2 3 
   
    
        


    


#     input = consume_input()
#     output = evaluate_input(input)
#     print(output)