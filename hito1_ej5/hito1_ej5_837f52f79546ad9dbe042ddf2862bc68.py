RUT=input("Ingrese su número de RUT sin puntos ni dígito verificador: ")
#Calculo
inverso_rut=RUT[::-1]
suma=0
serie = [2, 3, 4, 5, 6, 7]  # la serie numérica a usar

for i in range(len(inverso_rut)):
    digito = int(inverso_rut[i])
    suma += digito * serie[i % len(serie)]

resto = suma % 11
dv = 11 - resto

if dv == 11:
    dv = '0'
elif dv == 10:
    dv = 'K'
else:
    dv = str(dv)


print("dv=", dv)
