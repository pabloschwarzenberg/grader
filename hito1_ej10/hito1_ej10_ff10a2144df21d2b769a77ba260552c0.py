#Cajero Automático
usuario="10334151"
clave="1803"
saldo_inicial=int(1000000)
saldo_cuenta=int(100000)

def validar_clave(usuarioingresado,claveingresada):
    if claveingresada==clave:
        print("Bienvenido")
        monto_retirar=int(input("Ingrese su monto a retirar:"))
        if 0<monto_retirar<100000:
            finalcuenta=100000-monto_retirar
            finalcajero=1000000-monto_retirar
            print(finalcuenta)
            print(finalcajero)
        else:
            print("Monto no permitido")
        return True
    else:
        print("Clave Invalida")
        return False

intentos=3
while intentos>0:
      if __name__ == "__main__":
          usuario_ingresado=input("Ingrese su usuario:");
          clave_ingresada=input("Ingrese su clave:");
          if validar_clave(usuario_ingresado,clave_ingresada)is True:
              break
          else:
              intentos=intentos-1
if intentos==0:
    print("Tarjeta bloqueada")
    