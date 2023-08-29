#Ordenar tres números
n1 = int(input("Ingrese un 1er número: "))
n2 = int(input("Ingrese un 2do número: "))
n3 = int(input("Ingrese un 3er número: "))
if n2 <= n1 and n3 <= n2 :
 print("El orden de los números ordenados de menor a mayor es :" + str(n3) + "," + str(n2) + "," + str(n1))
elif n2 <= n3 and n1 <= n2 :
 print("El orden de los números ordenados de menor a mayor es :" + str(n1) + "," + str(n2) + "," + str(n3))
elif n3 <= n1 and n2 <= n3 :
 print("El orden de los números ordenados de menor a mayor es :" + str(n2) + "," + str(n3) + "," + str(n1))
elif n3 <= n2 and n1 <= n3 :            
 print("El orden de los números ordenados de menor a mayor es :" + str(n1) + "," + str(n3) + "," + str(n2))
elif n1 <= n2 and n3 <= n1 :
 print("El orden de los números ordenados de menor a mayor es :" + str(n3) + "," + str(n1) + "," + str(n2))
elif n1 <= n3 and n2 <= n1 :
 print("El orden de los números ordenados de menor a mayor es :" + str(n2) + "," + str(n1) + "," + str(n3))

