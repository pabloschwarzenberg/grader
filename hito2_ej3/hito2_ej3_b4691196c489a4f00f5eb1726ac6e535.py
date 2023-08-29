s = input("Ingrese un string: ")
n = int(input("Ingrese un entero n: "))

if len(s) < n:
    print("El largo del string es menor que n.")
else:
    substrings = {}
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    found_unique_substrings = False
    for substring in substrings:
        if substrings[substring] == 1:
            print(substring)
            found_unique_substrings = True
    
    if not found_unique_substrings:
        print("ninguna")
 