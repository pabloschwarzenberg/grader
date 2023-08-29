def unique_substrings(s, n):
    substrings = []
    counts = {}

    for i in range(len(s)-n+1):
        substr = s[i:i+n]
        substrings.append(substr)
        counts[substr] = counts.get(substr, 0) + 1

    unique_substrings = [substr for substr in substrings if counts[substr] == 1]

    return unique_substrings

s = input("Ingrese un string: ")
n = int(input("Ingrese un entero n: "))

result = unique_substrings(s, n)

if len(result) > 0:
    for substr in result:
        print(substr)
else:
    print("ninguna")