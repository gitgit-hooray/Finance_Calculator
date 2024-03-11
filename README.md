# Finance Calculator

## Description

This project is a financial calculator that provides two main functionalities:

&nbsp; &nbsp; &nbsp;*1. An investment calculator*
   
&nbsp; &nbsp; &nbsp;*2. A home loan repayment calculator*
     
The program allows users to calculate the interest earned on an investment or the monthly repayment amount for a home loan. 
It provides a simple and convenient way to perform financial calculations related to investments and home loans.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Screenshots](#screenshots)
    - [Main Program](#main-program)
    - [Output Results](#output-results)
- [Credits](#credits)

## Installation

To use this financial calculator locally, follow these steps:
<br>

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Finance_Calculator.git
   ```
   <br>
   
2. Navigate to the project directory:

   ```bash
   cd Finance_Calculator
   ```
   <br>
   
3. Run the financial calculator script from terminal, choose either script depending on requirements:

   a. This script is the original codebase with comments:
   
   ```bash
   python finance_calculator.py
   ```
   <br>
   b. This script is an alternative version with more detailed comments explaining the code:
   
   This is to improve the learning process and for more clarity on why certain code was used.

   ```bash
   python finance_calculators_extra_comments.py
   ```
   <br>
   c. This script is just the code without any comments:

   ```bash
   python justcode.py
   ```
   <br>
  
4. You can refer to the pseudocode file as an outline of the logic of the program using human-readable, informal language,
   facilitating algorithm development and clearer communication between developers.
   <br>

## Usage

After installing the project, you can use it as follows:

1. Choose between 'investment' or 'bond' based on your financial calculation needs.

2. Enter the required information when prompted, such as the deposit amount, interest rate, investment period, house value, interest rate for a bond,
   and the number of months for bond repayment.

3. The program will calculate and display the total interest for an investment or the monthly repayment amount for a home loan.

## Screenshots

### Main Program

This Python code represents a financial calculator program that provides users access to two distinct calculators:

   &nbsp; &nbsp; &nbsp;*1. An investment calculator*
   
   &nbsp; &nbsp; &nbsp;*2. A home loan repayment calculator*
<br>
1. The program incorporates while loops to continually prompt the user for numerical input, ensuring valid entries. Additionally, it defines a function, `obtain_numerical_input`, to handle repetitive input code. The user is presented with a welcoming introduction outlining the available calculators and their respective purposes, and the code employs the `math` module for mathematical operations.
<br>
<img width="703" alt="1" src="https://github.com/gitgit-hooray/finalCapstone/assets/151678204/d9dfe3cd-43f9-4502-b235-d224d2a37f43">
<br>
<br>
2. This Python code implements a financial calculator program with a user interface that operates within a while loop. The program prompts the user to choose between an investment calculator, a home loan repayment calculator, or to stop calculations altogether. Depending on the user's choice, it further prompts for relevant inputs such as deposit amount, interest rate, and duration. The program calculates either the simple or compound interest for investments or the monthly bond repayment amount based on the user's input. It incorporates error handling for invalid entries and continues to execute until the user chooses to stop.
<br>
<br>
<img width="989" alt="2" src="https://github.com/gitgit-hooray/finalCapstone/assets/151678204/ae3115aa-aa2e-40c5-b895-edaeea64736d">
<br>

### Output Results

#### Exiting Program

In this example, the user chose to end calculations by entering 'stop'. The program execution concludes, and the user returns to the command line interface.
<br>
<img width="719" alt="Exit program 1" src="https://github.com/gitgit-hooray/finalCapstone/assets/151678204/366bede2-a7b4-4cf7-9112-49c919b10bd2">

#### User inputs Investment & Simple Options

In this specific interaction, the user chose the 'investment' option. The program then prompts the user to input the deposit amount, interest rate, and the number of years for the investment. The user further selects that they want 'simple' interest. The program calculates and displays the total interest earned after the specified duration, based on the given inputs. In this example, the user deposited £50, with a 2% interest rate over 5 years, and opted for simple interest, resulting in a total interest of £55.0.
<br>
<img width="761" alt="Investment Simple" src="https://github.com/gitgit-hooray/finalCapstone/assets/151678204/ae7be6bc-36b0-4ab4-a839-f1fe75115003">

#### User inputs Investment & Compound Interest Options

The user selected the 'investment' option and provided inputs for the deposit amount (£50), interest rate (2%), and the investment duration (5 years). Additionally, the user opted for compound interest. The program then calculated and displayed the total interest earned after 5 years at a 2% interest rate, resulting in £55.2. This illustrates how the program dynamically responds to user inputs and performs calculations based on the selected options.
<br>
<img width="747" alt="Investment Compound" src="https://github.com/gitgit-hooray/finalCapstone/assets/151678204/1eb9a08d-f781-46e4-83c6-19a846a8f705">

#### Error Handling - User inputs wrong data for each prompt after inputting Investment 

The user initially selects the 'investment' option but enters invalid non-numerical values when prompted for the deposit amount, interest rate, and investment duration. The program correctly identifies these errors and requests valid numerical inputs. After the user provides the correct values, an additional error occurs when entering an invalid choice for the type of interest ('simple' or 'compound'). The program prompts the user to enter a valid option and continues the interaction until valid inputs are provided. This demonstrates the program's error handling and user guidance features, ensuring accurate data entry.
<br>
<img width="758" alt="Investment error handling" src="https://github.com/gitgit-hooray/finalCapstone/assets/151678204/8847e2db-f031-4d58-a8c8-4262d4405ed7">

#### User inputs Bond Option

The user chooses the 'bond' option and provides numerical inputs for the present value of their house (300,000), interest rate (3%), and the number of months for bond repayment (12). The program then calculates and displays the monthly bond repayment amount, which is £25,408.11. This illustrates the program's functionality in processing user inputs and performing accurate financial calculations based on the chosen option.
<br>
<img width="713" alt="Bond" src="https://github.com/gitgit-hooray/finalCapstone/assets/151678204/da311abc-faea-4f2a-b6bb-a31b7f92122a">

#### Error Handling - User inputs wrong data for each prompt after inputting Bond

The user selects the 'bond' option and is prompted to input the present value of their house, interest rate, and the number of months for bond repayment. The user initially enters invalid non-numerical values, but the program detects these errors and requests valid numerical inputs. Once the user provides correct values, the program calculates and displays the monthly bond repayment amount. Once again this demonstrates the program's error handling and the ability to guide the user through the correct input process for accurate calculations.
<br>
<img width="706" alt="Bond error handling" src="https://github.com/gitgit-hooray/Finance_Calculator/assets/151678204/b212c0a1-cb3c-40c5-8146-56cd9a17b859">


## Credits

This project was created by [Charmaine Fernandes](https://github.com/gitgit-hooray)
I appreciate the contributions and support from the open-source community.





