numeroT = int(input("Numero telefonico de 8 digitos: "))
horaLlamada = int(input("Hora de la llamada: "))

ultimosTresDigitos = numeroT % 10**3

regla1 = 0<= horaLlamada <= 7
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
regla2 = (14 < horaLlamada) or (ultimosTresDigitos == 909)
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
regla3 = (17<= horaLlamada <= 19) or (ultimosTresDigitos == 877)
#Después de las 19:00, no contestas el celular.
regla4 = horaLlamada <= 19

if (regla1 == True) or (regla2 == True) or (regla3 == True) or (regla4 == True):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")