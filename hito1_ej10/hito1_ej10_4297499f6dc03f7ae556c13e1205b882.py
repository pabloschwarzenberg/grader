#Cajero Automático
usu = int(input())
cla= int(input())
a = 0
sal = 1000000
if usu == 10334151 and cla == 1803:
  sald = 100000
  ret = int(input())
  print("saldo cuenta=", sald - ret)
  print("saldo cajero=", sal - ret)
elif cla != 1803:
  print("clave invalida")
  a = a + 1
if a == 3:
  print("tarjeta bloauqeada)
