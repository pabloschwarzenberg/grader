def obtener_substrings_unicos(string, n):
    substrings = {}
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr in substrings:
            substrings[substr] += 1
        else:
            substrings[substr] = 1
    
    unique_substrings = []
    for substr, count in substrings.items():
        if count == 1:
            unique_substrings.append(substr)
    
    return unique_substrings


if __name__ == "__main__":
    string = input("Ingresa el string: ")
    n = int(input("Ingresa el valor de n: "))
    substrings_unicos = obtener_substrings_unicos(string, n)
    if len(substrings_unicos) == 0:
        print("ninguna")
    else:
        for substr in substrings_unicos:
            print(substr)
      