def unique_substrings(s, n):
    substrings = set()
    unique_substrings = set()
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if substring in substrings:
            unique_substrings.discard(substring)
        else:
            substrings.add(substring)
            unique_substrings.add(substring)
    return unique_substrings

s = input("Ingresa un string: ")
n = int(input("Ingresa un entero n: "))

result = unique_substrings(s, n)

if len(result) == 0:
    print("ninguna")
else:
    for substring in result:
        print(substring)