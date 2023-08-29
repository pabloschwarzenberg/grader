##Programa pa cachar que signo del zodiaco eri
dia = eval(input('Ingrese solo el dia de cumpleaños:' ))
mes = eval(input('Ingrese mes de nacimiento\
(Solo 1 numero, 2 en caso de que sea necesario):' ))
if (21 <= dia <= 31 or 1 <= dia < 20) and (mes == 3 or mes == 4):
    signo = 'Aries'
elif (20 <= dia <= 31 or 1 <= dia < 21) and (mes == 4 or mes == 5):
    signo = 'Tauro'
elif (21 <= dia <= 31 or 1 <= dia < 21) and (mes == 5 or mes == 6):
    signo = 'Geminis'
elif (21 <= dia <= 30 or 1 <= dia < 23) and (mes == 6 or mes == 7):
    signo = 'Cancer'
elif (23 <= dia <= 31 or 1 <= dia < 23) and (mes == 7 or mes == 8):
    signo = 'Leo'
elif (23 <= dia <= 31 or 1 <= dia < 23) and (mes == 8 or mes == 9):
    signo = 'Virgo'
elif (23 <= dia <= 30 or 1 <= dia < 23) and (mes == 9 or mes == 10):
    signo = 'Libra'
elif (23 <= dia <= 31 or 1 <= dia < 22) and (mes == 10 or mes == 11):
    signo = 'Escorpio'    
elif (22 <= dia <= 30 or 1 <= dia < 22) and (mes == 11 or mes == 12):
    signo = 'Sagitario'
elif (22 <= dia <= 31 or 1 <= dia < 20) and (mes == 12 or mes == 1):
    signo = 'Capricornio'
elif (20 <= dia <= 31 or 1 <= dia < 19) and (mes == 1 or mes == 2):
    signo = 'Acuario'
elif (19 <= dia <= 29 or 1 <= dia < 21) and (mes == 2 or mes == 3): 
    signo = 'Piscis'
else:
    print('Error, fecha no valida')
print(signo)