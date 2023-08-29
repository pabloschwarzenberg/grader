#ENTRADA
x= int(input("ingrese un numero: "))
y= int(input("ingrese un numero: "))
z= int(input("ingrese un numero: "))
lista=[]

#PROCESO
if x<y and x<z:
    lista.append(x)
    if y<z:
        lista.append(y)
        lista.append(z)
    else:
        lista.append(z)
        lista.append(y)
elif y<x and y<z:
    lista.append(y)
    if x<z:
        lista.append(x)
        lista.append(z)
    else:
        lista.append(z)
        lista.append(x)
else:
    lista.append(z)
    if x<y:
        lista.append(x)
        lista.append(y)
    else:
        lista.append(y)
        lista.append(x)

    
print(lista)