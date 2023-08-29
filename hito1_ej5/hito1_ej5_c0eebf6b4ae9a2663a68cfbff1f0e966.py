#Cálculo del dígito verificador de un rut
rut = int(input("Ingresa tu rut sin el ultimo dijito: "))
 # paso 1
d8 = rut%10          #con %, accedo al último digito de rut. Pero no se lo saco.    
rut = rut//10        #con // le quito, el último dígito, y SOBREESCRIBO en rut. 

d7 = rut%10
rut = rut//10

d6 = rut%10
rut = rut//10

d5 = rut%10
rut = rut//10

d4 = rut%10
rut = rut//10

d3 = rut%10
rut = rut//10

d2 = rut%10
rut = rut//10

d1 = rut%10

#paso 2 y 3
suma = d8*2 + d7*3 + d6*4 + d5*5 + d4*6 + d3*7 +  d2*2 + d1*3
#paso 4
resto = suma%11
#paso 5
resultado = 11 - resto
#paso 6
if resultado == 11: #condicion a
    print("dv=0 ")
if resultado == 10: #condicion b
    print("dv=K ")
if resultado != 10 and resultado !=11: #condicion c
    print("dv=",resultado)