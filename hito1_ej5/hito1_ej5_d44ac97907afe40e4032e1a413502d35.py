#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese su rut sin puntos para conocer dígito verificador: "))
largo = len(rut)
mult = 2
contador = -1
sumatotal = 0
for i in rut:
     while i != 0:
            sumatotal = sumatotal + (int(rut[contador])*mult)
            contador -= 1
            mult += 1
            if mult > 7:
                mult = 2
            
            
            break

modulo = sumatotal//11
resto = sumatotal -(11*modulo)
final = 11 - resto
if final == 11:
    print("dv = "+"0")
elif final == 10:
    print("dv = "+"K")
else:
    print("dv ="+ str(final)) 