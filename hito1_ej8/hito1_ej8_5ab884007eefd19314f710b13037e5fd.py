numero=input()
if 0<=int(numero)<=9:
  print(numero[0],"U")
elif 10<=int(numero)<=99:
  print(numero[0],"D","+",numero[1],"U")
elif 100<=int(numero)<=999:
  print(numero[0],"C","+",numero[1],"D","+",numero[2],"U")
elif 1000<=int(numero)<=9999:
  print(numero[0],"M","+",numero[1],"C","+",numero[2],"D","+",numero[3],"U")