#Contestador de celular
numero=int(input("numero de telefono: "))
hora=int(input("hora: "))
ultimos3_digitos=numero%1000
if 0<hora<7:
  print("contestar")
if (hora<14 and ultimos3_digitos==909):
  print("contestar")
elif (17<hora<19 and 87800000>numero>87699999):
    print("no contestar")
elif (17<hora<19):
    print("contestar")
elif hora>19:
    print("no contestar")
else:
    print("no contestar")