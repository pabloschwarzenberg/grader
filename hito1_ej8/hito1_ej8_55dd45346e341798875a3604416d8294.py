#Descomponer un número
num = int(input("ingrese un número:"))
mil = num // 1000
num -= (1000*mil)
centena = num //100
num -= (100*centena)
decena = num // 10
num -= (10*decena)
unidad = num // 1

if mil == 0 and centena !=0:
  print("{}C + {}D + {}U".format(centena, decena, unidad))
elif mil == 0 and centena == 0:
  print("{}D + {}U".format(decena, unidad))
elif mil == 0 and centena == 0 and decena == 0:
  print("{}U".format(unidad))
else:
  print("{}M + {}C + {}D + {}U".format(mil, centena, decena, unidad))