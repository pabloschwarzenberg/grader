#Contestador de celular
from time import sleep
n_T = int(input("Ingrese número telefonico: "))
h_L = int(input("Ingrese la hora de llamada: "))
#primer if
while True:
  if h_L >=0 and h_L <=7:
    print("Contestar")
    sleep(1)
  if h_L < 14:
    if n_T%1000 == 909:
      print("Contestar")
      sleep(1)
      break
  if h_L>=17 and h_L <7:
    if n_T //1000==877:
      print("Contestar")
      sleep(1)
      break
  if h_L >19:
    print("NO CONTESTAR")
    break
  else:
    print("NO CONTESTAR")
    sleep(1)
    break