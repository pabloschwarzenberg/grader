texto = input("Ingrese un string")
lista = []
for i in texto:
        lista.append(i)
        if i=="A":
            lista.remove(i)
        if i=="C":
            lista.remove(i)
        if i=="G":
            lista.remove(i)
        if i=="T":
            lista.remove(i)

if len(lista) == 0:
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")