#Cajero Automático
intentos=3
usuario=3
while intentos>0:
    usuario=int(input("ingrese numero de usuario: "))
    if usuario==10334151:
        contrasena=int(input("ingrese contraseña: "))
        if contrasena==1803:
            opcion=int(input("ingrese su opcion (1: retira dinero, 2: saldo: "))
            if opcion==1:
               monto=int(input("Monto a retirar: "))
               if monto==45000:
                  print("saldo cuenta=55000")
                  print("saldo cajero=955000")
                  break
            elif opcion==2:
                print("saldo 100.000")
                break
        else:
            contrasena!=1803
            print("contraseña invalida")
            intentos=intentos-1
            if intentos==0:
               print("tarjeta bloqueada")
    else:
        usuario!=10334151
        print("usuario invalido")
