#Ordenar tres números
     
a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
c = int(input("Ingrese el tercer numero:"))

result1 = min(a, b, c)
result2 = max(a, b, c)
result3 = (a + b + c) - result1 - result2

print('Numero ordenados de menor a mayor son: {}, {} , {}'.format(result1, result3, result2))