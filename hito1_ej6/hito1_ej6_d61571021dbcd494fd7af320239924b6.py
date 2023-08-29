#Ordenar tres números
num1 = int(input('Escribe tu primer numero:'))
num2 = int(input('Escribe tu segundo numero:'))
num3 = int(input('Escribe tu tecer numero:'))

num_list = [num1 , num2, num3]
men_may = sorted(num_list)
print(*(men_may), sep = ',')