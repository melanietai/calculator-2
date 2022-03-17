"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)

from functools import reduce

while True:
    # ask user what they would like to calculate
    user_input = (input("What would you like to calculate?: "))
    # creating a tokenized list from user input
    token_input = user_input.split(" ")
    
    # if user presses q, exit calculator 
    if "q" in token_input:
        print("Exit")
        break

    # create variables for operator and list of nums to be calculated
    operator = token_input[0]
    nums = token_input[1:]

    result = None

    # make sure our user is inputting actual numbers!
    is_all_digit = True
    for i, num in enumerate(nums):
        if not num.isdigit():
            print("Sorry! You have to enter numbers!")
            is_all_digit = False
            break
        else:
            # convert numbers into float
            nums[i] = float(num)

    # if not all numbers, continue back loop to ask for user input        
    if not is_all_digit:
        continue

    # another way to convert to float: nums = [float(num) for num in nums]    

    # if user enter add, we call the add function, and repeat for other calculations
    # ex: + 2 3  
    if operator == "+":
        result = reduce(add, nums)

    # add subtraction operator 
    elif operator == "-":
        result = reduce(subtract, nums)
    
    # add multiplication operator
    elif operator == "*":
        result = reduce(multiply, nums)

    # add division operator 
    elif operator == "/":
        result = reduce(divide, nums)
    
    # add square operator
    elif operator == "square":
        result = reduce(square, nums)

    # add cube operator
    elif operator == "cube":
        result = reduce(cube, nums)
    
    # add power operator
    elif operator == "pow":
        result = reduce(power, nums)

    # add mod 
    elif operator == "mod":
        result = reduce(mod, nums)
    
    # add x+
    elif operator == "x+":
        result = reduce(add_mult, nums)
    
    # add cubes
    elif operator == "cubes+":
        result = reduce(add_cubes, nums)

    # else statement telling users to input operator and intergers...in case they didn't
    else:
        print("Please enter an operator followed by numbers.")

    print(result) 
        

   
    
        


    

