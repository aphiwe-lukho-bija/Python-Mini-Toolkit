# Python Mini Toolkit

A beginner-friendly command-line toolkit built in Python. It has 4 mini tools that solve small everyday problems. 
Made for my Python course to practice core programming concepts and show growth.

## Features

1. **Grade Calculator**  
   Enter multiple scores at once and get your average plus a letter grade.

2. **To-Do List**  
   Add, view, and remove tasks. Keeps running until you exit back to the main menu.

3. **Even/Odd Checker**  
   Checks if a number is even or odd, and whether it’s divisible by 5.  
   Uses the modulus operator with `and`/`or` logic.

4. **Daily Motivation Generator**  
   Prints a random motivational quote using Python’s `random` module.

## Python Concepts Used

- Variables, data types, user input, output, type casting
- Arithmetic, assignment, comparison, logical operators
- `if`, `elif`, `else` statements, nested conditions, boolean expressions
- `for` loops, `while` loops, `range`, loop control
- Functions, parameters, arguments, return values
- Lists and list comprehensions
- Built-in modules: `random`
- Custom modules: splitting code into `main.py` and `helpers.py`
- Bonus: Modulus operator combined with `and`/`or`

## How to Run

1. Make sure Python 3.8+ is installed
2. Clone this repo or download the files
3. Open terminal in the project folder
4. Run the program:
   5. Follow the on-screen menu to use each tool

## Challenges I Faced

The main issue was handling bad input. If a user typed text instead of a number, the program would crash.  
I fixed this by adding basic input checks and `try/except` blocks so the program stays running and gives a clear message instead.

## What I Learned

- How to organize code into multiple files using modules
- How to use loops and conditionals to build interactive menus
- The importance of testing with different types of input
- How to use GitHub to manage and share a project

## Author
Aphiwe Lukho Bija
