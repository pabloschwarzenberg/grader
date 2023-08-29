dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento (en formato numérico): "))

#Meses con 31 y 30 dias
m31d = [1, 3, 5, 7, 8, 10, 12]
m30d = [4, 6, 9, 11]
#Febrero tiene comunmente 28 dias, pero hay años que tiene 29
febrero = list(range(1,30)) 

#Analisis del mes y el dia colocado
while mes not in range(1,13):
  mes = int(input("El mes debe ser entre 1 y 12: "))
while mes in m31d and dia not in range(1,32):
  dia = int(input("El dia debe ser un valor entre 1 y 31: "))
while mes in m30d and dia not in range(1,31):
  dia = int(input("El dia deber ser un valor entre 1 y 30: "))
while mes==2 and dia not in febrero:
  dia = int(input("El dia deber ser un valor entre 1 y 29: "))

#Signos zodiaco
if (mes==12 and dia in range(22,32)) or (mes==1 and dia in range(1,20)):
  print("Tu signo zodiacal tropical es Capricornio")
elif (mes==1 and dia in range(20,31)) or (mes==2 and dia in range(1,19)):
  print("Tu signo zodiacal tropical es Acuario")
elif (mes==2 and dia in range(19,29)) or (mes==3 and dia in range(1,21)):
  print("Tu signo zodiacal tropical es Piscis")
elif (mes==3 and dia in range(21,31)) or (mes==4 and dia in range(1,20)):
  print("Tu signo zodiacal tropical es Aries")
elif (mes==4 and dia in range(20,31)) or (mes==5 and dia in range(1,21)):
  print("Tu signo zodiacal tropical es Tauro")
elif (mes==5 and dia in range(21,32)) or (mes==6 and dia in range(1,21)):
  print("Tu signo zodiacal tropical es Geminis")
elif (mes==6 and dia in range(21,31)) or (mes==7 and dia in range(1,23)):
  print("Tu signo zodiacal tropical es Cancer")
elif (mes==7 and dia in range(23,32)) or (mes==8 and dia in range(1,23)):
  print("Tu signo zodiacal tropical es Leo")
elif (mes==8 and dia in range(23,31)) or (mes==9 and dia in range(1,23)):
  print("Tu signo zodiacal tropical es Virgo")
elif (mes==9 and dia in range(23,31)) or (mes==10 and dia in range(1,23)):
  print("Tu signo zodiacal tropical es Libra")
elif (mes==10 and dia in range(23,32)) or (mes==11 and dia in range(1,22)):
  print("Tu signo zodiacal es Escorpio")
else:
  print("Tu signo zodiacal es Sagitario")