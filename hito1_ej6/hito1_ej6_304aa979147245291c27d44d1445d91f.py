#Ordenar tres números
print("\nNumeros de menor a mayor\n")

a=int(input("Escriba su primer numero entero: "))
b=int(input("Escriba su segundo numero entero: "))
c=int(input("Escriba su tercero numero entero: "))


maximo= max(a,b,c)
minimo= min(a,b,c)
medio= (a+b+c)- maximo - minimo

print ("\nLos numeros del menor al mayor son: ",minimo,",",medio,",",maximo)