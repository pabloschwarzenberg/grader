#Cálculo del dígito verificador de un rut
rut = eval(input("ingresa: "))
mult = 2
suma = 0
aux = rut
while aux > 0:
    n = aux%10
    aux = aux//10
    suma += (n * mult)
    if mult == 7:
        mult = 1
    mult += 1
mod = suma // 11
rest = suma - (mod*11)
dv = 11 - rest
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "k"
else:
    dv = dv
print("dv=",dv)