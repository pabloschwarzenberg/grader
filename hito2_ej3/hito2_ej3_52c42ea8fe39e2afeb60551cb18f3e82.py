def unique_substrings(string, n):
    substrings = {}
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        if substring not in substrings:
            substrings[substring] = 1
        else:
            substrings[substring] += 1
    
    unique_substrings = [substring for substring, count in substrings.items() if count == 1]
    
    if len(unique_substrings) > 0:
        for substring in unique_substrings:
            print(substring)
    else:
        print("ninguna")

# Ejemplos de uso
string = "ACGACG"
n = 3
unique_substrings(string, n)

string = "ACGACGAC"
n = 3
unique_substrings(string, n)

string = "AAAAA"
n = 3
unique_substrings(string, n)
   