#Calcular digito verificador
#Entradas
rut = input("Ingrese su rut sin digito verificador: ")

#Procesamiento
secuencia = "234567"
largo = len(rut)
suma = 0
dv = ""

#Iterador de ciclo
i = 0

while i < largo:
    suma = suma + int(secuencia[i % len(secuencia)]) * int(rut[-i-1])
    i += 1
dv = 11 - (suma % 11)

if dv == 10:
    print("dv=k")

elif dv == 11:
    print("dv=0")

else:
    print("dv=",+dv)     