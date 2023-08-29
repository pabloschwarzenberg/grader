#Cálculo del dígito verificador de un rut

rut= int(input("ingrese serie rut sin digito verificador : "))
suma=0
mult = 2

#ciclo
while rut > 0 :
    digito = rut % 10
    rut = rut//10
    suma += digito * mult
    if mult < 7 :
        mult += 1
    elif mult == 7 :
        mult = 2

modulo = suma / 11
modulo = int(modulo)
modulo_2 = suma - (11 * modulo)
modulo_final = 11 - modulo_2

if modulo_final == 11 :
    dig_v = 0
elif modulo_final == 10 :
    dig_v = "k"
else :
    dig_v = modulo_final

print("dv = " , dig_v)