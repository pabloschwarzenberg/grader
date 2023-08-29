#Cálculo del dígito verificador de un rut
#Cálculo del dígito verificador de un rut

rut = int(input("Ingrese RUT sin puntos, guíon y dígito verificador: "))

#Procesos

dig_8 = (rut //10000000)
dig_7 = (rut % 10000000) // 1000000
dig_6 = (rut % 1000000) // 100000
dig_5 = (rut % 100000) // 10000
dig_4 = (rut % 10000) // 1000
dig_3 = (rut % 1000) // 100
dig_2 = (rut % 100) // 10
dig_1 = rut % 10


calculo_digito = (dig_8*3)+(dig_7*2)+(dig_6*7)+(dig_5*6)+(dig_4*5)+(dig_3*4)+(dig_2*3)+(dig_1*2)

resto = calculo_digito // 11

resta = calculo_digito - (11*resto)

digito_verificador = 11 - resta

if digito_verificador == 11:
    print("DV=0")
elif digito_verificador == 10:
    print("DV=K")
else:
    print("DV=",digito_verificador)