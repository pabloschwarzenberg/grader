      def encontrar_substrings_unicos(s, n):
    substrings = set()
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if s.count(substring) == 1:
            substrings.add(substring)
    if not substrings and len(set(s)) == 1:
        return []
    return substrings

s = input("Ingrese un string: ")
n = int(input("Ingrese un entero n: "))

substrings_unicos = encontrar_substrings_unicos(s, n)

if not substrings_unicos:
    print("ninguna")
else:
    for substring in substrings_unicos:
        print(substring)