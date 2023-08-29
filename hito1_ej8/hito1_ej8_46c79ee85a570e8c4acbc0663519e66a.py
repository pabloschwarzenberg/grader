#Descomponer un número
numero=int(input('Ingrese un numero de hasta 4 digitos: '))
x=numero
d1=numero%10
numero=numero//10
d2=numero%10
numero=numero//10
d3=numero%10
numero=numero//10
d4=numero

if 0<= x < 10:
    rse=str(d1) + 'U'
    print(rse)
if 10 <= x < 100:
    rse=str(d2) + 'D + ' + str(d1) + 'U'
    print(rse)
if 100 <= x < 1000:
    rse=str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(rse)
if 1000 <= x < 10000:
    rse=str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(rse)
