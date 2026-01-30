# Question 4: Sorted Search with Conditions

from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

indices = []
for i in range(len(values)):
    if values[i] >= x:
        indices.append(i)

print("Sorted values:", values)
print("x:", x)

if len(indices) > 0:
    print("First matching index:", indices[0])
else:
    print("No value >= x")
