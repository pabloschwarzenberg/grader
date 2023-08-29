saldo_cajero=1000000
intentos=3
saldo_cuenta=100000
usuario_invalido=True
while usuario_invalido:
     usuario=input("Ingrese usuario: ")
     if usuario=="10334151":
         usuario_invalido=False
         print("Saldo cuenta=55000, saldo cajero=955000")
     else:
        usuario_invalido=True
        usuario=input("Ingrese usuario: ")
     if usuario=="10334151":
         clave_invalida=True
         clave=input("Ingrese clave: ")
     while clave_invalida:
      if clave=="1803":
         clave_invalida=False
      else:
         clave_invalida=True
         clave=input("Ingrese clave: ")


      if clave=="1803":
         monto=input("Ingrese monto a retirar: ")
         monto=int(monto)
         saldo_cuenta= saldo_cuenta - monto
         saldo_cajero= saldo_cajero - monto
         print("Saldo cuenta: ",saldo_cuenta,"Saldo cajero: ", saldo_cajero)
         salir=input("Desea Continuar")
         if salir=="n":
            usuario_invalido=True
            break
         else:
            usuario_invalido=False
            break

      else:
         intentos= intentos-1
         print("Clave invalida")
         if intentos==0:
             print("Tarjeta bloqueada")
         