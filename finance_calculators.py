"""
                This version is for task submission. 
For more detailed comments showing my understanding on the while loops 
            & functions in this code, please refer to the
            finance_calculators_extra_comments.py file 
which is for both evidence of understanding and educational purposes.

      This is a program that allows the user to access 
            two different financial calculators:
an investment calculator and a home loan repayment calculator.

""" 

import math
"""Function prevents the need for repetitive code."""
def obtain_numerical_input(prompt): 
    while True:
        # User continuosly prompted until numerical value entered. 
        user_input = input(f"Please enter {prompt}")
        if user_input.isdigit():
            return float(user_input)
        # If non-numerical value is entered, error message is displayed. 
        else:
            print("\nError: Please enter a numerical value without any other characters.\n")


introduction = """
\n\t\tWelcome to the Financial Calculator Page!\n
On this page you can use: \n
-An Investment Calculator
-A Home Loan Repayment Calculator\n
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan\n
"""

print(introduction)

stop_program = False
# 'not' operator causes statement to become True.
while not stop_program:
    choose = input("Enter either 'investment' or 'bond' from the menu above (or enter 'stop' to end calculations): ").lower()
    if choose == "stop":
        stop_program = True
        # True Boolean assigned, while loop becomes while not True, i.e. False. loop terminates.
    elif choose == "investment":
        deposit = obtain_numerical_input("the amount you wish to deposit: ")
        interest_rate = obtain_numerical_input("your interest rate as a percentage: ") / 100
    #             .strip(%) method can remove the '%' at the end if input, but unnecessary
    #           Strings can't be in calculations so '/ 100' is outside the string.
        years_invest = int(obtain_numerical_input("how many years you plan on investing: "))

        while True:
            interest = input("Please enter if you want 'simple' or 'compound' interest: ").lower()
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
    elif choose == "bond":
        house_value = int(obtain_numerical_input("the present value of your house: "))
        interest_rate = obtain_numerical_input("your interest rate: ") / 100 / 12
        repay_months = int(obtain_numerical_input("the number of months you plan to repay the bond: "))
        bond_repay = round((interest_rate * house_value) / (1 - (1 + interest_rate) ** - repay_months), 2)    
        repayment = print(f"\nThis is how much you'll have to repay each month: {bond_repay}")
    else:
        print("\n\t\t\tError: Invalid Entry\n\n\tPlease only enter either 'investment' or 'bond'.\n")
