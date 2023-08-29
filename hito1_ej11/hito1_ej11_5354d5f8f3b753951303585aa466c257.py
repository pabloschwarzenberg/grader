saldo_cajero=1000000
saldo_cta_cte=100000
user=10334151
psw=1803
usuario=int(input("Ingrese Usuario: "))
contador=1
while contador<=3:
  contraseña=int(input("Ingrese Contraseña :"))
  if (contraseña!=psw):
    print("datos Incorrectos, reintente")
    contador=contador+1
    if contador==3:
      print("Clave Bloqueda")
      contador=4
  else:
    contador=4
    giro=int(input("Ingrese Monto a Girar:"))
    if(giro>saldo_cta_cte):
      print("monto no permitido")
    else:
      miles = (giro%1000000-giro%100000)//100000
      centenas = (giro%100000-giro%10000)//10000
      decenas = (giro%10000-giro%1000)//1000
      print("saldo cuenta=",saldo_cta_cte-giro)
      print("saldo cajero=",saldo_cajero-giro)
      #print ("billetes 20000 = ",miles)
      print ("billetes 10000 = ",centenas)
      print ("billetes 5000 = ",decenas)
      