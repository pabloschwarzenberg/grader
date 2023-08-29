#Cajero Automático

intentos = 0
ingresado = False
saldo_cajero = 1000000
saldo_cuenta = 100000

while intentos < 3:
  usuario = input("Usuario: ")
  clave = input("Clave: ")
  if clave == "1803" and usuario == "10334151":
    ingresado = True
    break
  else:
    print("tarjeta bloqueada")

while ingresado == True:
  dinero_retirar = input("Monto a retirar: ")
  if dinero_retirar != "N":
  
  elif saldo_cuenta < int(dinero_retirar):
    print("monto no permitido")
  elif saldo_cajero < int(dinero_retirar):
    print("monto no permitido")
  else:
    saldo_cajero -= int(dinero_retirar)
    saldo_cuenta -= int(dinero_retirar)
    
    


  
