#Cálculo del dígito verificador de un rut
rut = int(input())
m = 2
c = len(str(rut))
sum = 0

while m <= 7 and c > 0:
    if m < 7:
        sum += int(str(rut)[c-1]) * m
        c -= 1
        m += 1
        
    else:
        sum += int(str(rut)[c-1]) * m
        c -= 1
        m = 2

entero = sum//11
resto = sum - (11 * entero)

verificador = str(11 - resto)

if verificador == "10":
    verificador = "k"
    
elif verificador == "11":
    verificador = "0"

print('dv=' + verificador)