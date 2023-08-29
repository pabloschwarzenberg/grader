#Descomponer un número
num = int(input('Ingresa un número de hasta 4 cifras: '))
respaldo=num
d1= num%10
num= num//10

d2= num%10
num= num//10

d3= num%10
num= num//10

d4= num%10

if 1<= respaldo <=9:
    cadena=str(d1)+'U'
    print(cadena)
if 10<=respaldo<=99:
    cadena = str(d2) + 'D + ' + str(d1) + 'U'
    print(cadena)
if 100<=respaldo<=999:
    cadena = str(d3)+'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(cadena)
    
if 1000<=respaldo<=9999:
    cadena = str(d4) + 'M + '  + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(cadena)
