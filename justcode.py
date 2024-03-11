import math

def obtain_numerical_input(prompt):
    while True:
        user_input = input(f"Please enter {prompt}")
        if user_input.isdigit():
            return float(user_input)
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

while not stop_program:
    choose = input("Enter either 'investment' or 'bond' from the menu above (or enter 'stop' to end calculations): ").lower()
    if choose == "stop":
        stop_program = True
    elif choose == "investment":
        P = obtain_numerical_input("the amount you wish to deposit: ")
        r = obtain_numerical_input("your interest rate as a percentage: ") / 100
        t = int(obtain_numerical_input("how many years you plan on investing: "))

        while True:
            interest = input("Please enter if you want 'simple' or 'compound' interest: ").lower()
            if interest == "simple":
                print(f"\nHere is the total amount of interest you will receive after {t} years at the {r}% interest rate: {round(P * (1 + r * t), 2)}\n")
                break  
            elif interest == "compound":
                print(f"\nHere is the total amount of interest you will receive after {t} years at the {r}% interest rate: {round(P * math.pow((1 + r), t), 2)}\n")
                break 
            else:
                print("\n\t\t\tError: Invalid Entry\n\n\tPlease only enter either 'simple' or 'compound'.\n")
    elif choose == "bond":
        P = int(obtain_numerical_input("the present value of your house: "))
        i = obtain_numerical_input("your interest rate: ") / 100 / 12
        n = int(obtain_numerical_input("the number of months you plan to repay the bond: "))
                
        repayment = print(f"\nThis is how much you'll have to repay each month: {round((i * P) / (1 - (1 + i) ** -n), 2)}\n")
            
    else:
        print("\n\t\t\tError: Invalid Entry\n\n\tPlease only enter either 'investment' or 'bond'.\n")
