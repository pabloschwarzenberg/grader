def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return False
    return True
secuencia = "ACTGactgGCTA"
print("¿Es válida?")
print(secuencia_valida(secuencia))      