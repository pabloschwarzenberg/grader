#Cálculo del dígito verificador de un rut
rut = int(input("ingrese su rut sin digito verificador: "))
rut_str = str(rut)[::-1]
total = 0
multiplo= [2, 3, 4, 5, 6, 7]
for i in range(len(rut_str)):
    total += int(rut_str[i]) * multiplo[i % 6]
resto = total % 11
digito_veri = 11 - resto
if digito_veri == 11:
    digito_veri = 0
elif digito_veri == 10:
    digito_veri = "K"
print("dv=" + str(digito_veri))    