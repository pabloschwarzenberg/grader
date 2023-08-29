      def obtener_substrings_unicos(string, n):
    substrings = []
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        count = string.count(substring)
        
        if count == 1:
            substrings.append(substring)
    
    return substrings

if __name__ == "__main__":
    string = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))
    
    substrings = obtener_substrings_unicos(string, n)
    
    if len(substrings) > 0:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")
