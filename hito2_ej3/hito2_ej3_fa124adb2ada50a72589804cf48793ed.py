def encontrar_substrings_unicos(string, n):
    freq_dict = {}

    for i in range(len(string) - n + 1):
        substring = string[i:i + n]

        freq_dict[substring] = freq_dict.get(substring, 0) + 1

    substrings_unicos = [substring for substring, freq in freq_dict.items() if freq == 1]

    return substrings_unicos

string_input = input("Ingrese el string: ")
n_input = int(input("Ingrese el valor de n: "))

substrings = encontrar_substrings_unicos(string_input, n_input)

if len(substrings) > 0:
    for substring in substrings:
        print(substring)
else:
    print("ninguna")