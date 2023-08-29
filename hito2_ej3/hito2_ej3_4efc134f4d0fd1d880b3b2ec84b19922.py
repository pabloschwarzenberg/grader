def encontrar_substrings_unicos(secuencia, n):
    substring_count = {}

    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i + n]
        if substring in substring_count:
            substring_count[substring] += 1
        else:
            substring_count[substring] = 1

    unique_substrings = [substring for substring, count in substring_count.items() if count == 1]
    return unique_substrings

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese el valor de n: "))

    unique_substrings = encontrar_substrings_unicos(secuencia, n)
    if unique_substrings:
        for substring in unique_substrings:
            print(substring)
    else:
        print("ninguna")
      