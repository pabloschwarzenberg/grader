#Ordenar tres números
a = int(input('Ingresa el primer numero: '))
b = int(input('Ingresa el segundo numero: '))
c = int(input('Ingresa el tercer numero: '))

Mx = max(a, b, c)
Min = min(a, b, c)
D = (a + b + c) - Mx - Min
print(Min , ' , ' ,D , ' , ', Mx)
  

