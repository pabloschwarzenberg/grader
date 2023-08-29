#Cálculo del dígito verificador de un rut
rutt = input('Ingresa el rut: ')

vecNumeros = [2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
vecNumRut = []

rutSplit = rutt.split('-')
rut = rutSplit[0]
cantDigitosRut = len(rut)
for i in range(cantDigitosRut):
    vecNumRut.append(rut[i])
vecNumRut.reverse()
acumulador = 0
for j in range(len(vecNumRut)):
    multi = int(vecNumRut[j]) * vecNumeros[j]
    acumulador = acumulador + multi
    #print("Suma= ",acumulador)
mod11 = acumulador % 11
#print("El MOD 11 es: ",mod11)
digitoVerificador = 11 - mod11

if digitoVerificador >= 1 and digitoVerificador <=9:
    dv = digitoVerificador
    print("dv=",dv)
else:
    if digitoVerificador == 10:
        dv = 'k'
        print("dv=",dv)
    else:
        dv = 0
        print("dv=",dv)