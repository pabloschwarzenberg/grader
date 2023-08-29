#Cajero Automático
saldoCajero = 1000000
saldoUsuario = 100000
Usuario = "10334151"
Clave = "1803"
intentos = 0
salir = False
while intentos < 3:
 if salir == True:
  break
 usuario = input("Ingrese el usuario")
 clave = input("Ingrese la clave")
 if usuario == Usuario and Clave == clave:
  while True:    
   monto = eval(input("Ingrese el monto"))
   bi20=20000
   bi10=10000
   bi5=5000
#$20000
   billetes20=monto // 20000
   aux=monto % 20000
#$10000
   billetes10=aux//10000
   aux=aux%10000
#$5000
   billetes5=aux// 5000
   aux=aux % 5000
   print("billetes 20000=",billetes20)
   print("billetes 10000=",billetes10)
   print("billetes 5000=",billetes5)   
   sumaBilletes=billetes10*bi10+billetes20*bi20+billetes5*bi5
   print("Monto retirado",sumaBilletes)
   if monto > saldoUsuario:
    print("monto no permitido")
   else:
    saldoUsuario = saldoUsuario - monto
    saldoCajero = saldoCajero - monto
    print("saldo cuenta=", saldoUsuario)
    print("saldo cajero=", saldoCajero)
   opcion = input("Desea Salir Y/N")
   if not(opcion == "N"):
    salir = True
    break     
 else: 
  print("clave invalida")
  intentos = intentos + 1
if intentos == 3:
 print("tarjeta bloqueada")      