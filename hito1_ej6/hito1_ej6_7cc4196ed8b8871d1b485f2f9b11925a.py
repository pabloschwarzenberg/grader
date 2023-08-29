#Ordenar tres números
x = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))
v = int(input("ingrese un numero: "))
MA = max(x,c,v)
MI = min(x,c,v)
medio = (x + c + v) - MA - MI
print("El numero de menor a mayor es: " , MI , "," , medio , "," , MA)