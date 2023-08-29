#Cálculo del dígito verificador de un rut
rut = input("Rut: ")
rut_invertido = rut[::-1]
serie = [2,3,4,5,6,7]
suma = 0

for i in range(len(rut_invertido)):
    suma += int(rut_invertido[i]) * serie[i%len(serie)]

n = 11 - (suma % 11)
if n == 11:
    dv = "0"
elif n == 10:
    dv = "K"
else:
    dv = str(n)
print("dv="+dv)