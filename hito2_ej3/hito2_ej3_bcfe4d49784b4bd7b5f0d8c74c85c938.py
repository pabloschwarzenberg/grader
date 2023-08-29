def substrings_unicos(s, n):
    count = {}
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if substring in count:
            count[substring] += 1
        else:
            count[substring] = 1

    unicos = []
    for substring, freq in count.items():
        if freq == 1:
            unicos.append(substring)

    if len(unicos) == 0:
        print("ninguna")
    else:
        for substring in unicos:
            print(substring)

# Ejemplo de uso:
s = input("Ingrese un string: ")
n = int(input("Ingrese el valor de n: "))
substrings_unicos(s, n)
