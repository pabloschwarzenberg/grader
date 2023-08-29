string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

substring2 = []
counts = {}

for i in range(len(string) - n + 1):
    substring = string[i:i+n]
    substring2.append(substring)
    counts[substring] = counts.get(substring, 0) + 1

unicos = [substring for substring in substring2 if counts[substring] == 1]

if unicos:
    for substring in unicos:
        print(substring)
else:
    print("ninguna")