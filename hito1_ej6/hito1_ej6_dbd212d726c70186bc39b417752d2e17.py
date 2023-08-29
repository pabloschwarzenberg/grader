x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de y: "))
z = int(input("ingrese el valor de z: "))

if x <= y and x <= z :
    menor = x

elif y < x and y < z:
    menor = y

else:
    menor = z
    
print("el numero menor es", menor)

if y >= x and y >= z:
    mayor = y
    
else:
     mayor = z

print("el numero mayor es", mayor) 

if y >= z and z >= x:
    medio = z
    
elif x > z and y > x:
    medio = x

else: medio = y

print("el numero de en medio es", medio)

print("el orden de los numeros de forma ascendente es:" ,menor,(","),medio,",", mayor)
    

