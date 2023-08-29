#Ordenar tres números
n1= int(input("Nro1: "))
n2= int(input("Nro2: "))
n3= int(input("Nro3: "))

maximo= max(n1,n2,n3)
minimo= min(n1,n2,n3)

print(maximo)
print(minimo)

d= (n1 + n2 + n3) -maximo - minimo #saca el valor central.

print("%s, %s, %s" %(minimo,d,maximo))
