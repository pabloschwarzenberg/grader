#Cálculo del dígito verificador de un rut

n = input("Ingrese rut para calcular digito verificador: ")
numero = 2
suma = 0
num = 2

for i in n[::-1]:
    if numero < 8:
        suma = suma + (numero * int(i))
        
        numero += 1
    elif numero >= 8:
        suma = suma + (num * int(i))
        num += 1
modulo = suma % 11
extra = 11 - modulo 

if extra == 11:
    dv = 0
elif extra == 10:
    dv = "K"
else:
    dv = extra 

print("dv = ",dv)
    