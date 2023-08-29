#Ordenar tres números
num1 = int(input('Ingresa un numero entero: '))
num2 = int(input('Ingresa un numero entero: '))
num3 = int(input('Ingresa un numero entero: '))
lista_num = []
lista_num = [num1, num2, num3]
lista_num.sort()
comas= ", ".join(map(str, lista_num))
print(comas)