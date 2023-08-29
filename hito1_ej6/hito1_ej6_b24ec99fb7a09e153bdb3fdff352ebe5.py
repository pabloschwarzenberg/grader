#Ordenar tres números
x = int(input("Ingrese 1° numero:"))
y = int(input("Ingrese 2° numero:"))
z = int(input("Ingrese 3° numero:"))

a = max(x,y,z)
b = min(x,y,z)
c = (x+y+z)-a-b

print("Los numeros ordenados son:"+str(b)+ ","+str(c)+ ","+str(a))        