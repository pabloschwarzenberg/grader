#Descomponer un número
num = int(input("ingrese numero de hasta 4 cifras: "))
if 0<num<10000:
  mil = num//1000
  cen= (num%1000)//100
  dec = ((num%1000)%100)//10
  uni = ((num%1000)%100)%10
  print(str(mil)+"M + "+str(cen)+"C + "+str(dec)+"D + "+str(uni)+"U")
else:
  print("Debe ser un número de hasta 4 cifras")      