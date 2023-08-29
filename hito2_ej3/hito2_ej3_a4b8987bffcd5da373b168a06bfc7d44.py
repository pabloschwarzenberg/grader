def substrings_unicos(s, n):
    substrings = [s[i:i+n] for i in range(len(s)-n+1)]
    unicos = []
    for substring in substrings:
        if substrings.count(substring) == 1:
            unicos.append(substring)
    return unicos

s = input("Ingresa un string: ")
n = int(input("Ingresa el largo de los substrings: "))
substrings = substrings_unicos(s, n)
if substrings:
    for substring in substrings:
        print(substring)
else:
    print("ninguna")
      