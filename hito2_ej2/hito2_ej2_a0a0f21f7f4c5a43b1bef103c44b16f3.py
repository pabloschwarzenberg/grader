def verificar(secuencia):
    lista = ["A","C","T","G"]
    Sal = None
    for i in secuencia:
        if i not in lista:
            Sal = False
        else:
            Sal = True
    return Sal
n = input("secuencia: ")
n = n.upper()
Res = verificar(n)
if Res == True:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")