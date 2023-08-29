#Cálculo del dígito verificador de un rut
# Entrada

num = int(input("Ingrese un RUT sin puntos ni digito verificador: "))

# Procesamiento
a = (num%10) * 2
b = ((num//10)%10) * 3
c = ((num//100)%10)*4
d = ((num//1000)%10)*5
e = ((num//10000)%10)*6
f = ((num//100000)%10)*7
g = ((num//1000000)%10)*2
h = ((num//10000000))*3

suma=(a+b+c+d+e+f+g+h)
resto = suma%11
resultado = 11-resto
if resultado == 11:
    dv = 0
    print("dv =", dv)
elif resultado == 10:
    dv = "K"
    print("dv =", dv)
else:
    dv = resultado
    print("dv =", dv)