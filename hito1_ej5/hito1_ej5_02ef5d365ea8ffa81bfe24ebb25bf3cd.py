rut = int(input("Ingrese su RUT: "))

if len(str(rut)) == 7:
    suma = int(str(rut)[0])*9 + int(str(rut)[1])*4 + int(str(rut)[2])*5 + int(str(rut)[3])*6 + int(str(rut)[4])*7 + int(str(rut)[5])*8 + int(str(rut)[6])*9
elif len(str(rut)) == 8:
    suma = int(str(rut)[0])*8 + int(str(rut)[1])*9 + int(str(rut)[2])*4 + int(str(rut)[3])*5 + int(str(rut)[4])*6 + int(str(rut)[5])*7 + int(str(rut)[6])*8 + int(str(rut)[7])*9
else:
    print("El rut es invalido")

dv = suma % 11


if dv == 10:
    dv = 'k'

print("dv="+str(dv))