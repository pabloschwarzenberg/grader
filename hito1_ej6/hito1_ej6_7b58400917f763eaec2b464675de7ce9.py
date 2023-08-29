#Ordenar tres números
#Almacenaré en 3 variables los numeros ingresados
x=int(input ("Ingrese primer numero:  "))
y = int(input ("Ingrese segundo numero:  "))
z = int(input ("Ingrese tercer numero:  "))
a = int (min(x, y, z))
c = int (max(x, y, z))
print (a, c)
#obtener el numero medio por medio de matematicas
b = int ((x + y + z)-a-c)
print ("Los numeros ordenados son:", a,',', b,',', c)
   