#Cálculo del dígito verificador de un rut
RUT=input("Ingrese el RUT sin puntos al que desea calcular el digito verificador: ")
x=len(RUT)

factor=2
total=0
while x>0:
    x = x -1
    digito = int(RUT[x:x+1])
    total = total + (digito * factor)
    if factor==7:
        factor=2
    else:
        factor = factor + 1
        
modulo11 = total%11
validacion = 11 - modulo11
if validacion==11:
    validacion=0
elif validacion==10:
    validacion="K"
else:
    validacion=validacion
print("dv=", validacion)