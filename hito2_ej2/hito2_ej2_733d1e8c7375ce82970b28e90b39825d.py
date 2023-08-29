def validarSecuencia(secuencia):
    for i in secuencia:
        if not i in "ACTG":
            return "secuencia incorrecta"
    return "secuencia correcta"
secuencia=input("Ingrese secuencia: ").upper()
print(validarSecuencia(secuencia))