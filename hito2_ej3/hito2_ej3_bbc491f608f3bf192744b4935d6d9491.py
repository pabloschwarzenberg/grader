s = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

substrings = set()
repeated_substrings = set()

for i in range(len(s) - n + 1):
    substring = s[i:i+n]
    if substring in substrings:
        repeated_substrings.add(substring)
    else:
        substrings.add(substring)

unique_substrings = substrings - repeated_substrings

if len(unique_substrings) == 0:
    print("ninguna")
else:
    for substring in unique_substrings:
        print(substring)