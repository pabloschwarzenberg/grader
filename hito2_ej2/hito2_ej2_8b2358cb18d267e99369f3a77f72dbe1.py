def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "ACTGactgGCTAactgb":
            return False
    return True


# Probar
secuencia = "ACTGactgGCTAactgb"
print("¿Es válida?")
print(secuencia_valida(secuencia))