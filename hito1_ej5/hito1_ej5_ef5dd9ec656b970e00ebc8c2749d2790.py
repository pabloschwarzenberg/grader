#Cálculo del dígito verificador de un rut
#Entradas------------------------------
RUT = int(input("Ingrese su run sin puntos y sin el dígito verificador: "))


#Variables-------
copia = RUT
dvp = 0
i = 2
#Condiciones---------
while copia > 0:
    digito = copia%10
    copia //= 10
    dvp += (digito*i)
    if i < 7:
        i += 1
    elif i == 7:
        i = 2

dvf = (dvp%11)
dvn = 11 - dvf
if dvn == 11:
    dv = 0
elif dvn == 10:
    dv = "k"
else:
    dv = dvn

#Salida---------------
print("dv =", dv)     

      