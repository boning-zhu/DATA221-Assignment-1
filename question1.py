# Question 1: Controlled Multiplication Loop

threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    currentNumber += 1
    product *= currentNumber

print("Final product:", product)
print("Number that caused exceed:", currentNumber)
