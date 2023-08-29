def unique_substrings(string, n):
    substrings = {}
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    unique_substrings = []
    
    for substring, count in substrings.items():
        if count == 1:
            unique_substrings.append(substring)
    
    return unique_substrings

string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

result = unique_substrings(string, n)

if len(result) == 0:
    print("ninguna")
else:
    for substring in result:
        print(substring)
