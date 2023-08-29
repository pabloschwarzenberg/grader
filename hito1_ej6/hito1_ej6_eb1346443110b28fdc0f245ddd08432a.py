#Ordenar tres numeros

a = eval(input('Ingresar primer numero: '))
b = eval(input('Ingresar segundo numero: '))
c = eval(input('Ingresar tercer numero: '))

x = max(a, b, c)
y = min(a, b, c)
z = (a + b + c) - x - y

print('Los numeros ordenados son' + str(y)+ ',' + str(z) + ',' + str(x))