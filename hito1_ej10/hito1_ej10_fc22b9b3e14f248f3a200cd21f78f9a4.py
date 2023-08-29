def saldo(monto, saldo_persona=100000,saldo_cajero=1000000):
  if monto>saldo_persona or monto>saldo_cajero:
    print('monto no permitido')
  if monto<=saldo_persona and monto<=saldo_cajero:
    saldo_persona-=monto
    saldo_cajero-=monto
    print('saldo cuenta=',str(saldo_persona))
    print('saldo cajero=',str(saldo_cajero))
   

intentos=1
clase=0
while True:
  if clase==0:
    print('Usuario')
    rut=input()
    print('Clave')
    clave1=input()
    if clave1=='1803':
      clase=1
    if clave1!='1803':
      print('clave invalida')
      intentos=1
    if intentos==3:
      print('tarjeta bloqueada')
      break
  if clase==1:
    print('ingrese un monto a retirar:')
    monto = input()
    frase = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
    if monto in frase:
      break
    elif monto == "N":
       clase = 1
    else:
      saldo(int(monto))
