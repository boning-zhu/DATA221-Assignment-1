# Question 5: Circle Area Comparison

import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Radii must be integers"

    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Radii must be positive"

    area1 = math.pi * radiusOfCircle1 ** 2
    area2 = math.pi * radiusOfCircle2 ** 2

    smaller = min(area1, area2)
    larger = max(area1, area2)

    percentage = (smaller / larger) * 100
    return percentage


print(circleAreaCoverage(3, 5))
