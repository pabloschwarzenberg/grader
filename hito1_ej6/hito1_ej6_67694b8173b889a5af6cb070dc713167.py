a = int(input('ingresa un numero: '))
b = int(input('ingresa un segundo numero: '))
c = int(input('ingresa un ultimo numero: '))

s = min(a, b, c)
t = max(a, b, c)
i = (a + b + c) - s - t

print('los numeros en ingresados en orden son: ' + str(s) +","+ str(i) +","+ str(t) )