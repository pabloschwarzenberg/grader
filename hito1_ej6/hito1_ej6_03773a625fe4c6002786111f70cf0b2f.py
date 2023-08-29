#Ordenar tres números
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
c = int(input("Ingrese nuevamente otro número entero: "))
     
x = min(a,b,c)
xx = max(a,b,c)
xxx = (a+b+c)-x-xx

print('de menor a mayor es:',x,',',xxx,',',xx)