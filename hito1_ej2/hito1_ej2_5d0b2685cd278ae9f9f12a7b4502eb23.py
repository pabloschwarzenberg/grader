#Contestador de celular
n=str(input("Ingrese el número de telefono (de 8 cifras)"))
h=int(input("Ingrese la hora de llamada (00:00-23:59)"))
inicio_3=int(n[0:3])
termino_3=int(n[-3:])
l=len(n)
if l!=8:
      print("Su número no es de 8 cifras")
else:
      if  0<=h<=7:
          print("CONTESTAR")
      elif 7<h<=14:
          if termino_3==909:
              print("CONTESTAR")
          else:
              print("NO CONTESTAR")
      elif 17<=h<=19:
          if inicio_3==877:
              print("NO CONTESTAR")
          else:
              print("CONTESTAR")
      elif h>19:
          print("NO CONTESTAR")
      else:
        print("NO CONTESTAR")