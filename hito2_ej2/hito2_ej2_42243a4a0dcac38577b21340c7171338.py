 def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return False
            print("secuencia incorrecta")
    return True
    print("secuencia correcta")


# Probar
secuencia = "ACTGactgGCTA"
print("¿Es válida?")
print(secuencia_valida(secuencia))  