ingreso = input("ingrese un numero: ")
x = len(ingreso)
factor = 2
total = 0
while x > 0;
	    x = x - 1
	numero = int(ingreso[x:x+1])
	total = total + (numero * factor)
	if factor == 7;
		factor = 2
	else:
		factor = factor + 1

modulo = total % 11
validador = 11 - modulo

if validador == 11: validador = 0
if validador == 10: validador = 1
print("dv= ";validador)


def dv(n):
    x = sum(list(n))
    e = math.floor(x / 11)
    f = x - (11 * e)
    h = 11 - f
    
    if (h == 11):
        h = "0"
    elif (h == 10):
        h = "k"
    return(h)

print("dv=",dv(calculo))