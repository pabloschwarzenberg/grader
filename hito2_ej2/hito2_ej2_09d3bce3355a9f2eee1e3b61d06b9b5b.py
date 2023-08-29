gen=input("ingrese secuencia:")
def valido(str):
    return str in ["A","C","T","G"]
def sec(str):
    for i in str:
        if not valido(i):
            x="secuencia incorrecta"
        else:
            x="secuencia correcta"
    return x
print(sec(gen))