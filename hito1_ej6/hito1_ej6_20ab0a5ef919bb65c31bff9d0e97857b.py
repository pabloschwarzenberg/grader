#Ordenar tres números
Numeros=[]
c=1
while True:
    try:
        x=int(input("ingrese numero: "))
        Numeros.append(x)
        c+=1
        if (c>3):
            break
    except ValueError:
        continue

Numeros=sorted(Numeros)

print("Numeros ordendos: ",Numeros)