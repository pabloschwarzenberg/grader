#Descomponer un número
#Entrada
numero = int(input("Ingrese un numero de hasta cuatro cifras: "))
resultado = numero

N1 = numero%10
numero = numero//10

N2 = numero%10
numero = numero//10

N3 = numero%10
numero = numero//10

N4 = numero%10
if 0 <= resultado < 10:
    Respuesta = str(N1) + 'U'
elif 10 <= resultado < 100:
        Respuesta = str(N2) + 'D +' + str(N1) + 'U'
elif 100 <= resultado < 1000:
        Respuesta = str(N3) + 'C +' + str(N2) + 'D +' + str(N1) + 'U'
elif 1000 <= resultado < 10000:
        Respuesta = str(N4) + 'M +' + str(N3) + 'C +' + str(N2) + 'D +' + str(N1) + 'U'

print(Respuesta)