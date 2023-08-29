#Ordenar tres números
arreglo=[0,0,0]
contador=0
while contador<3:
    print("Ingrese el numero",(contador+1),"de 3")
    numero=int(input(""))
    arreglo[contador]=numero
    contador+=1
arreglo.sort()
print(arreglo)