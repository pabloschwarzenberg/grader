#Descomponer un número
numero=round(float(input("Ingrese un número: ")))
mil=(numero//1000)
cen=((numero//100)%10)
dec=((numero//10)%10)
uni=(numero%10)
if 10000>numero>=1000:
  print(str(mil)+"M","+",str(cen)+"C","+",str(dec)+"D","+",str(uni)+"U")
elif 1000>numero>=100:
  print(str(cen)+"C","+",str(dec)+"D","+",str(uni)+"U")
elif 100>numero>=10:
  print(str(dec)+"D","+",str(uni)+"U")
elif 10>numero>=0:
  print(str(uni)+"U")