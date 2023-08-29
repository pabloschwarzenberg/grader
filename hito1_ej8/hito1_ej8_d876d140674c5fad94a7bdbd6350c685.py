#Descomponer un número
numero = int(input('Ingresa un numero de hasta 4 cifras: '))

Num = numero
d1 = numero%10
numero = numero//10

d2 = numero%10
numero = numero//10

d3 = numero%10
numero = numero//10

d4 = numero%10

if 0 <= Num < 10:
    respuestaSinEspacios = str(d1) + 'U'
    print(respuestaSinEspacios)
elif 10 <= Num <100:
    respuestaSinEspacios = str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)
elif 100 <= Num < 1000:
    respuestaSinEspacios = str(d3) + 'C +' + str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)
elif 1000 <= Num < 10000:
    respuestaSinEspacios = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)






  