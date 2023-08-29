#Ordenar tres números
 #Entrada

n1 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese otro número: "))
n2 = int(input("Ingrese otro número: "))

#Proceso
ma = max (n1,n2,n3)
mi = min (n1,n2,n3)
me = (n1 + n2 + n3) - ma - mi

#Salida

print("Los números ingresados de menor a mayor son: ", mi , " , ", me , " , ", ma)     