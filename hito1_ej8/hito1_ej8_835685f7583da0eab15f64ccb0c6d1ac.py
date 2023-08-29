#Descomponer un número
numero = int(input('ingresa un numero de hasta 4 cifras:' ))

respaldo = numero

d1 = numero%10
numero = numero//10

d2 = numero%10
numero = numero//10

d3 = numero%10
numero = numero//10

d4 = numero%10

if 1 <= respaldo <= 9:
    CadenaCaracteres = str(d1) + 'U'
    print(CadenaCaracteres)

if 10 <= respaldo <= 99:
    CadenaCaracteres = str (d2) + 'D + ' + str (d1) + 'U'
    print(CadenaCaracteres)

if 100 <= respaldo <= 999:
    CadenaCaracteres = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(CadenaCaracteres)

if 1000 <= respaldo <= 9999:
    CadenaCaracteres = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(CadenaCaracteres)
