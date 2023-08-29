secuencia = input("escriba la secuencia: ")
def validador(secuencia):
    secuencia = secuencia.lower()
    correctas = ["a","g","t","c"]
    c = 1
    for i in secuencia:
        if i not in correctas:
            c += 1
            return ("secuencia incorrecta")
        if c == len(secuencia) and i in correctas:
            return ("secuencia correcta")
        c += 1

print(validador(secuencia))
