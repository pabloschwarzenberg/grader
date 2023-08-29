#Ordenar tres números
n1 = int(input("Ingrese un numero cualquiera: ")) 
n2 = int(input("Ingrese un numero cualquiera: "))
n3 = int(input("Ingrese un numero cualquiera: "))

#Condicionales

if n1 <= n2 and n1 <= n3:
    nmenor = n1
    if n2 <= n3:
        nmedio= n2
        nmayor= n3
    else:
        nmedio = n3
        nmayor = n2

elif n2 <= n1 and n2 < n3:
    nmenor = n2
    if n1 <= n3:
        nmedio = n1
        nmayor = n3
    else:
        nmedio = n3
        nmayor = n1

else:
    nmenor = n3
    if n1 >= n2:
        nmedio = n1
        nmayor = n2
    else:
        nmedio = n2
        nmayor = n1

print(str(nmenor),",",str(nmedio),",",str(nmayor))

      