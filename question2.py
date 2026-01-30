# Question 2: Nested Dictionary from Strings

def analyze_strings(string_list):
    result = {}

    for s in string_list:
        length = len(s)
        if length % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        result[s] = {
            "length": length,
            "parity": parity
        }

    return result


# Test
words = ["data", "science"]
print(analyze_strings(words))
