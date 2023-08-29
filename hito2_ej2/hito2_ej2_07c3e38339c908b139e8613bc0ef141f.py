secuencia= input("Ingrese una secuencia: ")
aceptados= "agtcAGTC"

i=0
while i<len(secuencia):
    if secuencia[i] not in aceptados:
        print("Secuencia incorrecta")
        break

    i=i+1

if i==len(secuencia):
    print("Secuencia correcta")