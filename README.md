# Factorial-of-a-number-using-iteration
Factorial of a Number Using Iteration

This Python program calculates the factorial of a number using an iterative for loop.

📌 What is a Factorial?

The factorial of a number is the product of all positive integers less than or equal to that number.

Example:

5!=5×4×3×2×1=120

Special cases:

0! = 1
1! = 1
💻 Program Code
print("Factorial of a number using iteration\n")

num=int(input("Enter a number you want factorial of:"))

factorial=1

if num==0 or num==1:
    print("Factorial of",num,"is 1")

else:
    for i in range(1,num+1):
        factorial*=i    

print("Factorial of",num,"is",factorial)
🔍 How the Program Works
Takes a number as input from the user.
Initializes factorial variable to 1.
Checks if the number is 0 or 1.
If yes, factorial is 1.
Otherwise:
Uses a for loop from 1 to the given number.
Multiplies each value with factorial.
Prints the final factorial value.
▶ Example Output
Example 1
Enter a number you want factorial of: 5
Factorial of 5 is 120
Example 2
Enter a number you want factorial of: 0
Factorial of 0 is 1
🧠 Concepts Used
Variables
User Input
if-else Condition
for Loop
Arithmetic Operations
📖 Formula Used

n!=1×2×3×⋯×n

✅ Advantages of Iterative Method
Simple and beginner-friendly
Faster than recursion for large values
Avoids recursion stack overflow
⚠ Limitation
Factorial is only defined for non-negative integers.
Large numbers produce very large outputs.
