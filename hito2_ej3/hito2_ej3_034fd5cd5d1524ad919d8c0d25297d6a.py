def find_unique_substrings(string, n):
    substrings = []
    counts = {}

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        counts[substring] = counts.get(substring, 0) + 1

    for substring, count in counts.items():
        if count == 1:
            substrings.append(substring)

    return substrings

string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

substrings = find_unique_substrings(string, n)

if len(substrings) > 0:
    for substring in substrings:
        print(substring)
else:
    print("ninguna")