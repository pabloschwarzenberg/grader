def find_unique_substrings(s, n):
    substrings = {}
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    unique_substrings = [substring for substring, count in substrings.items() if count == 1]
    
    return unique_substrings     
string = input("Ingresa un string: ")
n = int(input("Ingresa un entero n: "))

unique_substrings = find_unique_substrings(string, n)

if len(unique_substrings) > 0:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")