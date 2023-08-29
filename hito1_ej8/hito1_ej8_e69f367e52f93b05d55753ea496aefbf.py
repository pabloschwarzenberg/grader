#Descomponer un número
numero=int(input('elige un numero de hasta 4 digitos: '))      
respaldo=numero

d1=numero%10
numero=numero//10

d2=numero%10
numero=numero//10

d3=numero%10
numero=numero//10

d4=numero%10

if 0<=respaldo<10:
    la_respuesta_Es=str(d1) + 'U'
if 10<= respaldo < 100:
    la_respuesta_Es= str(d2) + 'D + ' + str(d1) + 'U'
if 100<=respaldo<1000:
    la_respuesta_Es= str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
if 1000<=respaldo < 10000:
    la_respuesta_Es= str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + ' D + ' + str(d1) + 'U'

print(la_respuesta_Es)


