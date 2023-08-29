def obtener_substrings_unicos(string, n):
    substrings = []
    count = {}
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        if substring in count:
            count[substring] += 1
        else:
            count[substring] = 1

    for substring, frequency in count.items():
        if frequency == 1:
            substrings.append(substring)

    return substrings

string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

substrings_unicos = obtener_substrings_unicos(string, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")