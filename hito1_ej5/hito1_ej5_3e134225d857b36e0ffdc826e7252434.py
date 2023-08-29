#Cálculo del dígito verificador de un rut
from math import modf
import math

rut=int(input("Ingresar rut: "))
separar_numeros = [int(a) for a in str(rut)]
cantidad_digito=len(separar_numeros)


if cantidad_digito==8:

    digito_1=separar_numeros[0]
    digito_2=separar_numeros[1]
    digito_3=separar_numeros[2]
    digito_4=separar_numeros[3]
    digito_5=separar_numeros[4]
    digito_6=separar_numeros[5]
    digito_7=separar_numeros[6]
    digito_8=separar_numeros[7]

    mult_digito_8=digito_8*2
    mult_digito_7=digito_7*3
    mult_digito_6=digito_6*4
    mult_digito_5=digito_5*5
    mult_digito_4=digito_4*6
    mult_digito_3=digito_3*7
    mult_digito_2=digito_2*2
    mult_digito_1=digito_1*3
    suma_productos_1=mult_digito_1+mult_digito_2+mult_digito_3+mult_digito_4+mult_digito_5+mult_digito_6+mult_digito_7+mult_digito_8
    dividir_suma=suma_productos_1/11
    parte_entera=math.trunc(dividir_suma)
    resto_division=suma_productos_1-(11*parte_entera)
    digito_verificador=11-resto_division
    dv_1=0
    if digito_verificador==11:
        dv_1=0
        print ("dv=" + str (dv_1))
    if digito_verificador==10:
        dv_1="K"
        print ("dv=" + str (dv_1))
    if digito_verificador!=11 and digito_verificador!=10:
        dv_1=digito_verificador
        print ("dv=" + str (dv_1))

    
if cantidad_digito==7:

    digito_1=separar_numeros[0]
    digito_2=separar_numeros[1]
    digito_3=separar_numeros[2]
    digito_4=separar_numeros[3]
    digito_5=separar_numeros[4]
    digito_6=separar_numeros[5]
    digito_7=separar_numeros[6]

    mult_digito_7=digito_7*2
    mult_digito_6=digito_6*3
    mult_digito_5=digito_5*4
    mult_digito_4=digito_4*5
    mult_digito_3=digito_3*6
    mult_digito_2=digito_2*7
    mult_digito_1=digito_1*2
    suma_productos_1=mult_digito_1+mult_digito_2+mult_digito_3+mult_digito_4+mult_digito_5+mult_digito_6+mult_digito_7
    dividir_suma=suma_productos_1/11
    parte_entera=math.trunc(dividir_suma)
    resto_division=suma_productos_1-(11*parte_entera)
    digito_verificador=11-resto_division
    dv_2=0
    if digito_verificador==11:
        dv_2=0
        print ("dv=" + str (dv_2))
    if digito_verificador==10:
        dv_2="K"
        print ("dv=" + str (dv_2))
    if digito_verificador!=11 and digito_verificador!=10:
        dv_2=digito_verificador
        print ("dv=" + str (dv_2))     