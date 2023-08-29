#Cajero Automático

usuario=10334151
clave=1803
saldo_cajero=1000000
saldo=100000
monto=int(input())

def cajero_automatico(saldo,saldo_cajero):
    global saldo_cajero
    global saldo
    intentos=3
    clave=int(input())
    while intentos>0:
      if clave_ingresada==clave:
        print("Seleccione monto a retirar")
          global monto
          if monto<=100000:
            saldo=saldo-monto
            saldo_cajero=saldo_cajero-monto
            return(saldo)
            return(saldo_cajero)
            print("saldo cuenta=",saldo,",saldo cajero=",saldo_cajero)
          else:
            print("Monto no permitido")
            return False
      else:
        while intentos>0:
          if not clave_ingresada==clave:
            intentos=intentos-1
          else:
            print("Tarjeta Bloqueada")
            break
        if intentos==0
          print ("Tarjeta Bloqueada")
