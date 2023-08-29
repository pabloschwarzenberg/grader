#Ordenar tres números

n=int(input("Ingrese un numero:"))
print("El numero ingresado es " ,n)


m=int(input("Ingrese un numero:"))
print("El numero ingresado es " ,m)


if n>m:
    
    mayor_1=n
    mayor_2=m
    print("Los numeros ordenados de menor a mayor son " , mayor_2,mayor_1)
    
else:
    
    mayor_1=m
    mayor_2=n
    print("Los numeros ordenados de menor a mayor son " , mayor_2,mayor_1)


o=int(input("Ingrese un numero:"))
print("El numero ingresado es " ,o)

mayor_3=o

if o >= mayor_1:
    
    print(mayor_2, mayor_1, mayor_3,sep= ",")
    

elif o <= mayor_2:
    print(mayor_3,mayor_2,mayor_1,sep= ",")

elif o > mayor_2 and o < mayor_1:
    print(mayor_2,mayor_3,mayor_1,sep= ",")

else:
    print("no se puede ordenar")