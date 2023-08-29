#Contestador de celular
tel= input("Ingrese un numero telefonico de 8 digitos: ")
hora= int(input("Ingrese hora de la llamada: "))
num8= tel[-1]
num7= tel[-2]
num6= tel[-3]
num3= tel[-6]
num2= tel[-7]
num1= tel[-8]
finalstr= num6+num7+num8
iniciostr= num1+num2+num3
finalint= int(finalstr)
inicioint= int(iniciostr)
if hora >= 0 and hora <= 7:
  print("CONTESTAR")
elif hora < 14 and finalint == 909:
  print("CONTESTAR")
elif hora < 14 and finalint != 909:
  print ("NO CONTESTAR")
elif hora >= 17 and hora <= 19 and inicioint == 877:
  print ("NO CONTESTAR")
elif hora >= 17 and hora <= 19 and inicioint != 877:
  print("CONTESTAR")
elif hora > 19:
  print ("NO CONTESTAR")
else:
  print ("NO CONTESTAR")