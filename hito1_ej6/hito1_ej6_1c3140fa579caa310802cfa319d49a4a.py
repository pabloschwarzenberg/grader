#Ordenar tres números
x=[]
for i in range(3):
  x.append(int(input('Ingrese un numero:')))
x.sort()
print('Los numeros ingresados de menor a mayor son:', str(x))