#Ordenar tres números
x = int(input("introdusca el primer numero: "))
y = int(input("introdusca el segundo numero: "))
z = int(input("introdusca el tercer numero: "))

if((x <= y) and (x <= z)):
    menor = x
    if(y <= z):
        medio = y
        mayor = z
    else:
        medio = z
        mayor = y
elif((y <= x) and (y < z)):
    menor = y
    if(x <= z):
        medio = x
        mayor = z
    else:
        medio = z
        mayor = x
else:
    menor = z
    if(x <= y):
        medio = x
        mayor= y
    else:
        medio = y
print("asi se ordenarian los numeros de menor a mayor: ",menor,"," , medio,"," , mayor)
