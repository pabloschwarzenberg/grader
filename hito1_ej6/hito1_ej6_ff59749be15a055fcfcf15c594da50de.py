#Ordenar tres números
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese un número entero: "))
c = int(input("Ingrese un número entero: "))

min = min(a,b,c)
max = max(a,b,c)
med = (a+b+c)-(min+max)

print(min,",",med,",",max)

      