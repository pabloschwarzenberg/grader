     def encontrar_substrings_unicos(cadena, n):
    substrings = {}
    for i in range(len(cadena) - n + 1):
        substr = cadena[i:i+n]
        if substr in substrings:
            substrings[substr] += 1
        else:
            substrings[substr] = 1

    unique_substrings = [substr for substr, count in substrings.items() if count == 1]
    return unique_substrings


if __name__ == '__main__':
    cadena = input("Introduce una cadena: ")
    n = int(input("Introduce el valor de n: "))

    unique_substrings = encontrar_substrings_unicos(cadena, n)

    if len(unique_substrings) > 0:
        for substr in unique_substrings:
            print(substr)
    else:
        print("ninguna")
 