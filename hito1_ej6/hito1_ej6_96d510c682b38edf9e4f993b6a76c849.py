#Ordenar tres números
n1=eval(input("ingrese un numero:"))
n2=eval(input("ingrese un numero:"))
n3=eval(input("ingrese un numero:"))
maximo=max(n1,n2,n3)
minimo=min(n1,n2,n3)
o=(n1+n2+n3)- maximo - minimo
print("el orden de menor a mayor es", minimo, ",", o, ",",maximo)