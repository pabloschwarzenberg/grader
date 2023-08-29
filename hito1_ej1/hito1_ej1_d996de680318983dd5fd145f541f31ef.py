#Nota final
notas=int(input("ingrese numeros de notas:"))
suma=0
i=1
while (i<=notas):
    print("ingrese la nota numero:", i)
    nota=float(input())
    suma=suma+nota
    i+=1
promedio=suma/nota
print("el promedio de nota es:", promedio)
    
      