rut = int(input("Ingresa tu rut: "))

multi = 2
utr = str(rut)[::-1]
suma = 0
for i in str(utr):
    suma += int(i) * multi
    multi +=1
    if(multi > 7):
        multi = 2

modulo = suma // 11

modulo *= 11
faltante = suma - modulo
faltante = 11 - faltante
digito_verificador = ""
if(faltante < 10):
    digito_verificador = faltante
elif(faltante == 10):
    digito_verificador = "K"
else:
    digito_verificador = "0"

print("dv=",digito_verificador)
