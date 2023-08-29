#Contestador de celular
n = input("ingresar numero telefonico:")
h = float(input("hora de la llamada:"))
lista = [n]
if 0<h and h<=7:
  print("Contestar")
elif h<14 and h>7:
  if n[5]=="9" and n[6]=="0" and n[7]=="9":
    print("Contestar")
  else:
    print("No contestar")
elif 17<h and h<19:
  if n[0]=="8" and n[1]=="7" and n[2]=="7":
    print("No contestar")
  else:
    print("Contestar")
else:
  print("No contestar")