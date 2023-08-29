#Cálculo del dígito verificador de un rut.

rut = int(input("Por favor, ingrese su rut sin dígito verificador: "))

#Asignación de variables.

_rut = str(rut) # Transformo a str para combinar con otras funciones.
largo_rut = len(_rut)
multiplicador = 2
suma_resultado = 0
dv = 0
#Condiciones.

while largo_rut > 0:
    suma_resultado = suma_resultado + (int(_rut[largo_rut-1])* multiplicador)
    

    if multiplicador < 7:
        multiplicador += 1
    elif multiplicador == 7:
        multiplicador = 2

    largo_rut -= 1
#Planteamos la fórmula para calcular el dig_verificador.
    
modulo = 0
modulo = suma_resultado - ((suma_resultado // 11) * 11)

dv = 11 - modulo

if dv == 11:
    print("dv=0")    
elif dv == 10:
    print("dv=k")
else:
    print("dv="+str(dv))
    