 def obtener_substrings_unicos(string, n):
    substrings = {}

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

    unique_substrings = [substring for substring, count in substrings.items() if count == 1]
    return unique_substrings


if __name__ == "__main__":
    string = input("Ingresa el string: ")
    n = int(input("Ingresa el valor de n: "))

    unique_substrings = obtener_substrings_unicos(string, n)

    if len(unique_substrings) > 0:
        for substring in unique_substrings:
            print(substring)
    else:
        print("ninguna")
     