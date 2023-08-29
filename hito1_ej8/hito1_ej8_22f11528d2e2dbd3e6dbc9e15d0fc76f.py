num = eval(input('Ingrese numero de cuatro cifras: '))

num1 = num % 10000 // 1000

num2 = num % 1000 // 100

num3 = num % 100 // 10

num4 = num % 10

print(str(num1) + 'M ' + '+ ' + str(num2) + 'C ' + '+ ' + str(num3) + 'D ' + '+ ' + str(num4) + 'U')