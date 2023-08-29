#Ordenar tres números
list_num = []
num1 = int(input('ingrese numero entero uno: '))
list_num.append(num1)
num2 = int(input('ingrese numero entero dos: '))
list_num.append(num2)
num3 = int(input('ingrese nuemro entero tres: '))
list_num.append(num3)
list_num.sort()
sep = ','
print(list_num[0], sep, list_num[1], sep, list_num[2], end=' ')