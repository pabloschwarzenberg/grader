 def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return False
    return True


# Probar
secuencia = "ACTGactgGCTA"
print("¿Es válida?")
print(secuencia_valida(secuencia)