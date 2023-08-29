#Ordenar tres números
a = int(input("Ingrese primer valor: "))
b = int(input("Ingrese segundo valor: "))
c = int(input("Ingrese tercer valor: "))

x = min(a, b, c)
y = max(a, b, c)
z = (a + b + c) - x - y

#1, 2, 3
#x = 1
#y = 3
#z = (1 + 2+ 3) - 1 - 3
#z = 2

print("El orden es: {}, {}, {}".format(x, z, y))

  
     
 

