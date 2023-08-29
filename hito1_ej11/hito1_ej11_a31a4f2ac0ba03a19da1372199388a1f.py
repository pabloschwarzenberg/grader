#Cajero Automático

usuario = "10334151"
clave = "1803"
saldocajeroinicial=1000000
saldocuentainicial=100000

def validar_clave(usuario,clave_ingresada):
  if clave_ingresada==clave:
    return True
  else:
    return False

intentos = 3

while intentos > 0:
  usuario_ingresado = input()
  clave_ingresada = input()
  if not validar_clave(usuario_ingresado,clave_ingresada):
    intentos = intentos - 1
  else:
    monto=float(input())
    
    global saldocajeroinicial
    global saldocuentainicial
    
    if monto > saldocuentainicial:
      print("monto no permitido")
    else:
      saldocajerofinal=saldocajeroinicial - monto
      saldocuentafinal=saldocuentainicial - monto
      
      print("saldo cuenta=",saldocuentafinal)
      print("saldo cajero=",saldocajerofinal)
    break
    
if intentos == 0:
    print("tarjeta bloqueada")