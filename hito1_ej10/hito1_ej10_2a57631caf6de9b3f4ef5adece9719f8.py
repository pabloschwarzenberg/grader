#Cajero Automático
saldoCajero=1000000
usuarioValido=10334151
claveValida=1803
saldoCuenta=100000

usuario=int(input("ingrese usuario:"))
while usuario!=usuarioValido:
    usuario=int(input("ingrese usuario nuevamente:"))


clave=int(input("ingrese clave:"))
intentos=0
while clave != claveValida:
    intentos = intentos+1
    if intentos == 3:
        print("tarjeta bloqueada")
        break
    clave=int(input("clave invalida;"))
    
if intentos != 3:#continuo con el programa si  la clave no esta bloqueada
    montoRetirado=int(input("ingrese monto:"))
    if montoRetirado>saldoCajero or montoRetirado>saldoCuenta:
        print("monto no permitido")
    else:
        saldoCajero=saldoCajero-montoRetirado
        saldoCuenta=saldoCuenta-montoRetirado
        print("saldoCuenta=",saldoCuenta)
        print("saldoCajero=",saldoCajero)
        
      