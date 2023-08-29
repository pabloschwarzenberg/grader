def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return False
    return True


# Probar
secuencia = input("ingrese una secuencia:")
print("¿Es válida?")
print(secuencia_valida(secuencia))