def validacionCadena(cadena):
    for letra in cadena:
        if not letra.upper() in "ACTG ":
            return "secuencia incorrecta"
    return "secuencia correcta"


cadena = input("Ingrese cadena a comprobar: ")

print(validacionCadena(cadena))