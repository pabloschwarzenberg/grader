#Ordenar tres números
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero 2: "))
c=int(input("Ingrese un numero 3: "))
ma= max(a,b,c)
mi= min(a,b,c)
d= (a+b+c) - ma - mi
print(mi, ",", d ,",",ma)