#Contestador de celular
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular.
N = int(input("Ingrese numero de celular:"))
H = int(input("Ingrese la hora de llamada:"))

pn = N // 100000
u3 = N % 1000
if (H >= 00) and (H <= 7):
    print("CONTESTAR")

if (H >= 8) and (H <= 14) or (u3 == 909):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")

if (H >= 15) and (H <= 16):
    print("NO CONTESTAR")
if (H >= 17) and (H <= 19):
    print("CONTESTAR")
elif (H >= 15) and (H <= 19) or (pn == 877):
    print("NO CONTESTAR")

if (H >= 20) and (H <= 00):
    print("NO CONTESTAR")