#Descomponer un número
numero = int(input('Ingresa un número de hasta 4 cifras: '))

respaldo = numero

d1= numero%10
numero = numero//10

d2= numero%10
numero = numero//10

d3= numero%10
numero = numero//10

d4= numero%10

if 1 <= respaldo <= 9:
    cadenaDeCaracteres = str(d1) + 'U'
    print(cadenaDeCaracteres)

if 10 <= respaldo <= 99:
    cadenaDeCaracteres = str(d2) + 'D + ' + str(d1) + 'U'
    print(cadenaDeCaracteres)

elif 100 <= respaldo <= 999:
    cadenaDeCaracteres = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(cadenaDeCaracteres)

elif 1000 <= respaldo <= 9999:  
    cadenaDeCaracteres = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(cadenaDeCaracteres)