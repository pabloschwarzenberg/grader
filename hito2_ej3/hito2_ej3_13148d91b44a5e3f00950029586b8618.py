def encontrar_substrings_unicos(string, n):
    substrings = set()
    repeated_substrings = set()

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
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

# Ejemplo de uso
string = input("Ingresa el string: ")
n = int(input("Ingresa el valor de n: "))

encontrar_substrings_unicos(string, n)
      