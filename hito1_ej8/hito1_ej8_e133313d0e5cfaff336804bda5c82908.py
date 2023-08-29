#Descomponer un número
numero=int(input("Ingrese un número de hasta 4 dígitos: "))
unidades=numero-(numero//10)*10
decenas=(numero-(numero//100)*100-unidades)//10
centenas=(numero-(numero//1000)*1000-decenas*10-unidades)//100
miles=(numero-(numero//10000)*10000-centenas*100-decenas*10-unidades)//1000
if miles!=0:
  print(miles,"M+",centenas,"C+",decenas,"D+",unidades,"U")
elif miles==0 and centenas!=0 and decenas!=0 and unidades!=0:
  print(centenas,"C+",decenas,"D+",unidades,"U")
elif miles==0 and centenas==0 and decenas!=0 and unidades!=0:
  print(decenas,"D+",unidades,"U")
elif miles==0 and centenas==0 and decenas==0 and unidades!=0:
  print(unidades,"U")
elif miles==0 and centenas==0 and decenas==0 and unidades==0:
  print("0")
elif miles!=0:
  print(miles,"M+",centenas,"C+",decenas,"D+",unidades,"U")
elif miles==0 and centenas!=0:
  print(centenas,"C+",decenas,"D+",unidades,"U")
elif miles==0 and centenas==0 and decenas!=0:
  print(decenas,"D+",unidades,"U")
elif miles==0 and centenas==0 and decenas==0 and unidades!=0:
  print(unidades,"U")