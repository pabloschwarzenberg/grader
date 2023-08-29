#Ordenar tres números
num = eval(input('ingrese un número: '))
num2 = eval(input('ingrese otro número: '))
num3 = eval(input('ingrese un último número: '))

ma = max(num,num2,num3)
mi = min(num,num2,num3)
d = (num + num2 + num3) - ma - mi

print(mi, ",", d, ",", ma)