def unique_substrings(s, n):
    substr_count = {}
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substr_count:
            substr_count[substring] += 1
        else:
            substr_count[substring] = 1
    
    unique_substrings = [substr for substr, count in substr_count.items() if count == 1]
    
    if unique_substrings:
        for substr in unique_substrings:
            print(substr)
    else:
        print("ninguna")

# Obtener la entrada del usuario
s = input("Ingresa el string: ")
n = int(input("Ingresa el valor de n: "))

# Llamar a la función
unique_substrings(s, n)
