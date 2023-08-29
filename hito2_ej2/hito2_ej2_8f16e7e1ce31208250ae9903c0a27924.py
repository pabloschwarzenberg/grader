# validar secuencias de adn

adn = input("Ingrese el ADN: ")

valido = True
for letra in adn:
    if letra.upper() not in "ACTG":
        valido = False
        break

if valido:
    print("La secuencia", adn, "es correcta")
else:
    print("La secuencia", adn, "es incorrecta")


# subsecuencia de adn

def obtener_substrings_unicos(string, n):
    substrings = []
    unique_substrings = []
    
    # Obtener todos los substrings de largo n
    for i in range(len(string) - n + 1):
        substrings.append(string[i:i+n])
    
    # Encontrar los substrings que aparecen una única vez
    for substring in substrings:
        if substrings.count(substring) == 1:
            unique_substrings.append(substring)
    
    return unique_substrings

