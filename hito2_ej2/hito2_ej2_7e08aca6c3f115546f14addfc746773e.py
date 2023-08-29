def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg" and "ACTG":
            return False
    return True


# Probar
secuencia = input("Ingrese secuencia: ")
print("¿Es válida?")
print(secuencia_valida(secuencia))
   