def encontrar_substrings_unicos(secuencia, n):
    """
    Esta función recibe una secuencia de ADN en forma de string y un entero n, y devuelve una lista con todos los
    substrings de largo n que aparecen una única vez en la secuencia.
    """
    # Creamos un diccionario donde almacenaremos la cantidad de veces que aparece cada substring de largo n
    sub_counts = {}
    for i in range(len(secuencia) - n + 1):
        sub = secuencia[i:i+n]
        sub_counts[sub] = sub_counts.get(sub, 0) + 1
    
    # Filtramos el diccionario para obtener los substrings que aparecen una sola vez
    substrings_unicos = [sub for sub, count in sub_counts.items() if count == 1]
    
    return substrings_unicos


secuencia = input("Introduce la secuencia de ADN: ")
n = int(input("Introduce el largo de los substrings a buscar: "))

substrings_unicos = encontrar_substrings_unicos(secuencia, n)

if not substrings_unicos:
    print("ninguna")
else:
    for sub in substrings_unicos:
        print(sub)
