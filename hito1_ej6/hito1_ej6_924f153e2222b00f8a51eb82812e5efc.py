#Ordenar tres números
x = int(input("ingrese primer numero:"))
y = int(input("ingrese segundo numero:"))
z = int(input("ingrese tercer numero:"))
mayor = max (x,y,z)
menor = min (x,y,z)
medio = (x + y + z) - menor - mayor
print (menor, ",", medio, ",", mayor)