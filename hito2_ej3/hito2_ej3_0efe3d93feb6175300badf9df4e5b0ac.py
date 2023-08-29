def obtener_substrings(s, n):
    substrings = []

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if s.count(substring) == 1:
            substrings.append(substring)

    return substrings

if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese el valor de n: "))

    substrings = obtener_substrings(s, n)

    if len(substrings) > 0:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")

