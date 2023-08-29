#Contestador de celular
fono=int(input("Ingrese número telefónfico de 8 cifras: "))
termina=fono%1000
comienza=fono//100000
hora=input("Ingrese hora en formato hh: ")

#Desarrollo"
if hora >="00" and hora <="07":
  print("CONTESTAR")
elif hora <"14" and termina == 909:
  print("CONTESTAR")
elif hora >="17" and hora <="19" and comienza != 877:
  print("CONTESTAR")
elif hora > "19":
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")