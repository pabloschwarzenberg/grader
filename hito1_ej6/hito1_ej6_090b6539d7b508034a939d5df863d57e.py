#Ordenar tres números
num1 = int(input("escriba su primer numero: "))
num2 = int(input("escriba su segundo numero: "))
num3 = int(input("escriba su tercer  numero: "))
mi = min(num1, num2, num3)
ma = max(num1, num2, num3)
d = (num1 + num2 + num3 ) - mi - ma


print(mi,",", d,",", ma ) 