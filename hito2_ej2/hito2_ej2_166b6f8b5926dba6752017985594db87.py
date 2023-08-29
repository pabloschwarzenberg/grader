
def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            resultado= "La secuencia {} es incorrecta"
            return (resultado.format(secuencia))
    resultado= "La secuencia {} es correcta"
    return (resultado.format(secuencia))


# Probar
secuencia= input()
print(secuencia_valida(secuencia))