def find_unique_substrings(string, n):
    substrings = set()
    unique_substrings = set()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring in substrings:
            unique_substrings.discard(substring)
        else:
            substrings.add(substring)
            unique_substrings.add(substring)
    
    return unique_substrings

string = input("Ingresa el string: ")
n = int(input("Ingresa el entero n: "))

unique_substrings = find_unique_substrings(string, n)

if unique_substrings:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")
