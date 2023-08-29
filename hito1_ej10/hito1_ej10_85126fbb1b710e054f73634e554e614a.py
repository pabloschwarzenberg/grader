saldo_inicial=1000000
dinero_usuario=100000
contraseña=1803
nombre_usuario=10334151
intentos=0
true=True
while intentos<3:
    usuario=int(input("numero de usuario: "))
    clave=int(input("ingrese su clave: "))
    if clave!=contraseña and usuario==nombre_usuario:
        intentos=intentos+1
        print("clave invalida")
    elif clave==contraseña and usuario==nombre_usuario:
        break
    elif intentos==3:
          print("clave invalida, tarjeta bloqueada")

while true==True :
    monto=int(input("monto a retirar: "))
    dinero_usuario=dinero_usuario-monto
    saldo_inicial=saldo_inicial-monto
    if monto>dinero_usuario:
        print("monto no permitido")
        dinero_usuario=dinero_usuario+monto
        saldo_inicial=saldo_inicial+monto
    elif monto <=dinero_usuario:
        print("saldo cuenta= ",dinero_usuario)
        print("saldo cajero= ",saldo_inicial)
        continuar=input("desea hacer otra operacion?" )
    if continuar!="N":
        true=False
    