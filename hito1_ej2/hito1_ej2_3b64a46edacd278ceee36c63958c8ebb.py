#Contestador de celular
nt = int(input("Ingresar numerro de hasta 8 digitos: "))
hora = int(input("Ingresar hora de 0 a 23 hrs: "))
r = "NO CONTESTAR"
nt678 = nt%1000
nt123 = nt//100000
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
if(hora < 7 and hora >= 0) : r = "CONTESTAR"
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
if(hora <= 14 and hora >= 7 and nt678 == 909) : r = "CONTESTAR"
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
if(hora >= 17 and hora <= 19 and nt123 != 877) : r = "CONTESTAR"
#Después de las 19:00, no contestas el celular.
print(r)
