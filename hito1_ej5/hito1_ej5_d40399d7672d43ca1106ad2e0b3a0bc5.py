#Cálculo del dígito verificador de un rut

rut = int(input("Ingrese RUT sin puntos, guíon y dígito verificador: "))

#Procesos

dig_8 = rut // 10000000
dig_7 = (rut - (dig_8 * 10000000)) // 1000000
dig_6 = (rut % 1000000) // 100000
dig_5 = (rut % 100000) // 10000
dig_4 = (rut % 10000) // 1000
dig_3 = (rut % 1000) // 100
dig_2 = (rut % 100) // 10
dig_1 = rut % 10

# Multiplicación de los digitos
mdig_1 = dig_1 * 2
mdig_2 = dig_2 * 3 
mdig_3 = dig_3 * 4
mdig_4 = dig_4 * 5
mdig_5 = dig_5 * 6
mdig_6 = dig_6 * 7
mdig_7 = dig_7 * 2
mdig_8 = dig_8 * 3

#Suma de dígitos
suma = mdig_1 + mdig_2 + mdig_3 + mdig_4 + mdig_5 + mdig_6 + mdig_7 + mdig_8

#Módulo 11 a suma
m11 = suma // 11

#resta y múltiplicación de módulo por 11
resta = suma - (m11 * 11)

#11 menos la resta
resultado = 11 - resta

#Dígito verificador
if resultado == 11:
    print("dv=0")
elif resultado == 10:
    print("dv=k")
elif resultado == resultado:
    print("dv=",resultado)