genoma=input("ingrese secuencia:")
def valido(string):
    return string in ["A","C","T","G"]
def secuencia(string):
    for letra in string:
        if not valido(letra):
            X="secuencia incorrecta"
        else:
            X="secuencia correcta"
    return X
print(secuencia(genoma))
