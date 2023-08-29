#Cálculo del dígito verificador de un rut
rut = input("ingrese su rut sin punto ni digito verificador: ")
newrut = rut[::-1]
x = 2
suma = 0
for i in newrut:
    suma += int(i) * x 
    x += 1
    if x == 8:
        x = 2
resto = suma / 11
resto = int(resto)
digito = 11 - (suma - resto * 11)
if digito == 11:
    print("dv=0")
elif digito == 10:
    print("dv=k")
else:
    print("dv={}".format(digito))   