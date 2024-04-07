import random

FIXED_LENGTH = 3

def generateLists(n):
    output = []
    for _ in range(n):
        curr = []
        for _ in range(FIXED_LENGTH):
            curr.append(random.randint(0, 100))

        maximum = max(curr)
        output.append((curr, maximum))

    return output

print(generateLists(5))


