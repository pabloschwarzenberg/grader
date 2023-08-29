#Cajero Automático

  intento<=3   
  monto_dinero_cajero=1000000
  usuario=int(input("ingrese usuario: "))
  clave=int(input("ingrese clave: "))
  monto_sacar_usuario=int(input("ingrese monto a retirar: "))
  monto_dinero_usuario=100000
          

if (usuario==10334151) and (clave==1803):
    print("clave valida")
    if (monto_sacar_usuario<=monto_dinero_usuario):
        monto_dinero_usuario=monto_dinero_usuario-monto_sacar_usuario
        monto_dinero_cajero=monto_dinero_cajero-monto_dinero_usuario
        print("te queda",monto_dinero_usuario)
        print("el cajero tiene",monto_dinero_cajero)
elif: 
    ("ingreso invalido")
    intento-1
    else:
        intento=3
        print("tarjeta bloqueada")
        break
    


