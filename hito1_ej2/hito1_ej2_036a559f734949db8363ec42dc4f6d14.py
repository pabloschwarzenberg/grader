#Contestador de celular
from time import sleep

num_tel= int(input("ingrese numero de telefono: "))
hora= int(input("ingrese hora de la llamada: "))
while True:
  if hora>=0 and hora<=7:
    print("CONTESTAR")
    sleep(1)
  if hora<14:
    if num_tel%1000==909:
      print("CONTESTAR")
      sleep(1)
      break
  if hora>=17 and hora<=19:
    if num_tel//1000==877:
      print("CONTESTAR")
      sleep(1)
      break
  if hora>19:
    print("NO CONTESTAR")
    break
  else:
    print("NO CONTESTAR")
    sleep(1)
    break