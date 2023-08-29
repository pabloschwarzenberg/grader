def encontrar_substrings_unicos(s, n):
    substrings = set()
    count = {}
    
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if substring in substrings:
            count[substring] = count.get(substring, 0) + 1
        else:
            substrings.add(substring)
    
    unicos = [substring for substring in substrings if count.get(substring, 0) == 0]
    
    return unicos

if __name__ == "__main__":
    s = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))
    
    substrings_unicos = encontrar_substrings_unicos(s, n)
    
    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
      