"""

This version is for educational purposes, it includes more detailed 
        comments to show further understanding of concepts 
                like while loops and functions.
      This is a program that allows the user to access 
            two different financial calculators:
an investment calculator and a home loan repayment calculator.

"""

import math

"""
      The 'obtain_numerical_input()' function is created & defined
             because it can be called many times, any time.
  In this case, it's called each time the program asks for the correct 
               numerical data when prompting user input.
          It prevents having to write and use repetitive code 
    (see alternative repetitive while loop code below in docstring.)
          This makes the code more DRY (Don't Repeat Yourself).
"""


def obtain_numerical_input(prompt):

    # 'while True', starts the while loop. If the user enters a non-numerical
    #   value, an error message is displayed, and the loop continues until
    #       a valid numerical value is entered. Then the loop exits
    #  through the return statement and outputs the result of the function
    #         so a break statement is not needed to break the loop.

    while True:
        #  'user_input', stores user's input that the prompt asks for.
        #       'input(prompt)' is for general user input whereas
        # 'obtain_numerical_input(prompt)' is to ensure numerical input.
        """
        The .isdigit function makes sure the string input is only digits.
        """
        user_input = input(f"Please enter {prompt}")
        if user_input.isdigit():
            return float(user_input)
        #           There doesn't need to be a break or continue statement after
        #             the return statement because once return is encountered,
        # the function stops executing, and the control is passed back to the calling code.
        #         The while True loop is effectively ended by the return statement.
        else:
            print("\nError: Please enter a numerical value without any other characters.\n")
             # The break statement is intentionally left out so that the while loop,
             # loops until the user enters a numerical value.


# '\n' & '\t' used to improve readability.
# For readability and to write cleaner code you can store the following long
# 'non-calculations' text in a variable named "introduction", and print
# this variable rather than having to use the print function for each line.

introduction = """
\n\t\tWelcome to the Financial Calculator Page!\n
On this page you can use: \n
-An Investment Calculator
-A Home Loan Repayment Calculator\n
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan\n
"""

print(introduction)

#     The stop_program variable stores a False Boolean. When called
#    in a while loop with a 'not' operator the statement becomes True.
# When the variable is in the while loop it translates to while not False.
#   When the user enters 'stop' upon the prompt input, the stop_program
#    variable is assigned a True Boolean and the while loop translates
#   to while not True, i.e. False. This stops the loop and the program.

stop_program = False

while not stop_program:
    choose = input("\nEnter either 'investment' or 'bond' from the menu above (or enter 'stop' to end calculations): ").lower()
    """
              If the user enters the words with capitals, the program 
             won't recognise the input because Python is case sensitive 
                so the .lower() method is used to convert them.
            The users input string must match the programs exact value 
        of "investment" or "bond", otherwise the code will not be carried out.
    """
    if choose == "stop":
        stop_program = True
    elif choose == "investment":
        deposit = obtain_numerical_input("the amount you wish to deposit: ")
        interest_rate = obtain_numerical_input("your interest rate as a percentage: ") / 100
        """
                      If the user enters a numerical value with '%' at the end, 
                    the .strip(%) method can be used to remove the '%' at the end. 
            This is because Python will not be able to do calculations with non-integers.
         i.e r = obtain_numerical_input("your interest rate as a percentage: ").strip(%) / 100
                         However this is only applicable and neccessary if 
                the obtain_numerical_input() function and while True loop is not used, 
                      and correct user input is checked for just this variable.
        """
        #         You can't divide the user's input by 100 within the brackets as you
        #        can't divide a string by an integer. First you must convert the input
        #                from a string to a float then divide by 100 after.
        #                    A string can't participate in calculations.
        years_invest = int(obtain_numerical_input("how many years you plan on investing: "))

        while True:
            interest = input("\nPlease enter if you want 'simple' or 'compound' interest: ").lower()
            if interest == "simple":
                simple_return = round(deposit * (1 + interest_rate * years_invest), 2)
                print(f"\n Total interest after {years_invest} years at the {interest_rate}% interest rate: {simple_return} \n")
                break  # If no break statement, the while loop continues as it's always True.
            elif interest == "compound":
                compound_return = round(deposit * math.pow((1 + interest_rate), years_invest), 2)
                print(f"\n Total interest after {years_invest} years at the {interest_rate}% interest rate: {compound_return} \n")
                break
            else:
                print("\n\t\t\tError: Invalid Entry\n\n\tPlease only enter either 'simple' or 'compound'.\n")
                 # The break statement is intentionally left out so that the while loop,
                 # loops until the user enters 'simple' or 'compound'.

    elif choose == "bond":
        house_value = int(obtain_numerical_input("the present value of your house: "))
        interest_rate = obtain_numerical_input("your interest rate: ") / 100 / 12
        repay_months = int(obtain_numerical_input("the number of months you plan to repay the bond: "))
        bond_repay = round((interest_rate * house_value) / (1 - (1 + interest_rate) ** - repay_months), 2)
        repayment = print(f"\nThis is how much you'll have to repay each month: {bond_repay}")
    
        # The break statement is intentionally left out so that after
        # the calculation is done the while loop, returns and loops back
        # to the start to ask the user to input another choice of calculation
    else:
        print("\n\t\t\tError: Invalid Entry\n\n\tPlease only enter either 'investment' or 'bond'.\n")
        # The break statement is intentionally left out so that the while loop,
        # loops until the user enters 'investment' or 'bond'.


"""
        This is the code containing the repetitive while loops 
            for getting numerical input from the user 
    when the wrong data is entered i.e. non-numerical characters.


if choose == "investment":
    while True: 
        p = input("Please enter the amount you wish to deposit: ")
        if p.isdigit():
            P = float(p)
            break # If user enters a numerical value the loop is broken
        else:
            print("\nError: Please enter a numerical value without any other characters.\n")
    while True:
        R = input("Please enter your interest rate as a percentage: ")
        if R.isdigit():
            r = float(R) / 100
            break 
        else:
            print("\nError: Please enter a numerical value without '%' or any other characters.\n")
    while True:
        T = input("Please enter how many years you plan on investing: ")
        if T.isdigit() :
            t = int(T)
            break
        else:
            print("\nError: Please enter a numerical value without any other characters.\n")
    interest = input("Please enter if you want 'simple' or 'compound' interest: ").lower()
    if interest == "simple":
        print(f"Here is the total amount of interest: {round(P * (1 + r * t), 2)}")
    elif interest == "compound":
        result = print(f"Here is the total amount of interest: {round(P * math.pow((1 + r), t), 2)}")
elif choose == "bond":
    P = int(input("Please enter the present value of your house: "))
    i = float(input("Please enter your interest rate: ")) / 100 / 12
    n = int(input("Please enter the number of months you plan to repay the bond: "))
    repayment = print(f"This is how much you'll have to repay each month: {round((i * P) / (1 - (1 + i) ** -n), 2)}")
else:
    print("Error: Invalid Entry\n")
    print("Please only enter either 'investment' or 'bond'.")
    
"""

