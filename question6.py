# Question 6: Distribution Analysis

def distribution_analysis(numbers):
    result = {}
    total = len(numbers)

    for value in set(numbers):
        count = 0
        for n in numbers:
            if n <= value:
                count += 1
        result[value] = (count / total) * 100

    return dict(sorted(result.items()))


numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))
