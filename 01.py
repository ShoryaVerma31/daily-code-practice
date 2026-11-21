"""Question 1
Write a program to print the sum of all odd digits and some of all even digits of a number?
What is the time and space complexity of your code."""

num = int(input("Enter the number: "))

oddSum = 0
evenSum = 0

while (num > 0):
    digit = num % 10

    if (digit % 2 == 0):
        evenSum = evenSum + digit

    else:
        oddSum = oddSum + digit

    num = num // 10

print(f"Some of all even digits of a number: {evenSum}")
print(f"Some of all odd digits of a number: {oddSum}")

'''
Time Complexity: O(log n)
Because the number is divided by 10 in each iteration.

Space Complexity: O(1)
Because only a constant number of variables are used.
'''

