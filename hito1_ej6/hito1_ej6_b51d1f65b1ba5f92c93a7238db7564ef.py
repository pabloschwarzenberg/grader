#Ordenar tres números
x=int(input("Escriba el primer número: "))
y=int(input("Escriba el segundo número: "))
z=int(input("Escriba el tercer número: "))

a = min(x , y ,z)
b = max(x , y ,z)
c =(x + y + z)- a -b

print("Los valores ordenados de menor a mayor son: ", a ," ,", c , " , " , b ,)