#Contestador de celular
numero= input("Ingrese el numero ")
hora = int(input("Ingrese la hora "))
if 7 < hora< 14 and numero[-1] == "9" and numero[-2] == "0" and numero[-3] == "9":
  print("CONTESTAR")
elif 17 <= hora <= 19 and numero[0] == "8" and numero[1] == "7" and numero[2] == "7":
  print("NO CONTESTAR")
elif 17 <= hora <= 19:
  print("CONTESTAR")
elif 0 <= hora <= 7:
  print("CONTESTAR")
elif hora > 19 :
  print("NO CONTESTAR")
elif 7 < hora < 14: 
  print("NO CONTESTAR")



