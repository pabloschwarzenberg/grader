#Contestador de celular
#Escribe un programa para contestar automáticamente el celular, dependiendo de la hora en que llega la llamada y el número de teléfono. El número telefónico debe ser representado por un número entero (int) de 8 cifras (por ejemplo 78735653), mientras que la hora es representada por un número entero entre 0 y 23. Las reglas que rigen si contestarás o no son las siguientes:
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular.
#entrada:
n=int(input("ingrese número telefonico:"))
h=int(input("ingrese hora de la llamada:"))
#desarrollo:
N1=(n//100)%10
N2=(n//10)%10
N3=n%10
n1=str(N1)+str(N2)+str(N3)
n2=n//100000
if n<10000000:
  print("ingrese otro número")
  n=int(input("número:"))
elif h<0 and h>23:
  print("ingrese la hora correctamente")
  h=int(input("hora:"))
elif n>=10000000 and h>=0 and h<=7:
  print("CONTESTAR")
elif n>=10000000 and h<=14 and n1==str(909):  
  print("CONTESTAR")
elif n>=10000000 and h<=14:
  print("NO CONTESTAR")
elif n>=10000000 and h>14 and h<17:
  print("NO CONTESTAR")
elif n>=10000000 and h>=17 and h<=19 and n2==877:
  print("NO CONTESTAR")
elif n>=10000000 and h>=17 and h<=19:
  print("CONTESTAR")
elif n>=10000000 and h>19:
  print("NO CONTESTAR")