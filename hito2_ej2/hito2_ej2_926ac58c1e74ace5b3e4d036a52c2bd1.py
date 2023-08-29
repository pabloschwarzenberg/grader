def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return print("secuencia incorrecta")
    return print("secuencia correcta")


# Probar
secuencia = str(input("Ingrese una secuencia: "))
secuencia_valida(secuencia)