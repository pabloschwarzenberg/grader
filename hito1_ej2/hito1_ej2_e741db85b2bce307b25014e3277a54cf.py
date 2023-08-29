#Contestador de celular
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular.

a=input("ingrese numero telefonico")
b=float(input("ingrese hora de la llamada"))
if 0<=b<=7:
   print ("Resultado:CONTESTAR")
elif 7<=b<=14 and a[5:8]=="909":
   print("Resultado:CONTESTAR")
elif 17<=b<=19 and a[0:3]!="877":
   print("Resultado:CONTESTAR")
elif 19<b<=24:
   print("Resultado:NO CONTESTAR")
else:
   print("Resultado:NO CONTESTAR")

   