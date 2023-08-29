#Contestador de celular
num= int(input("Ingrese número de teléfono: "))


hora= int(input("Ingrese hora: "))

if num >= 100000000 or num <=9999999:
  print("NO VÁLIDO")
else:

  num1=str(num)

  if hora >= 0 and hora <= 7:
    print("CONTESTAR")
  elif hora > 14 and num1[5:8] != 909:  
    print("NO CONTESTAR")
  elif hora >= 17 and hora <= 19 and num1[0:3] != 877:
    print("NO CONTESTAR")
  elif hora > 19:
    print("NO CONTESTAR") 
  else:
    print("CONTESTAR")     