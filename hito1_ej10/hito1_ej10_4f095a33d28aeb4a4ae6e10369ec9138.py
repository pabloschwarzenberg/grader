#Cajero Automático
Saldo_cajero=int(1000000)
Saldo_cuenta=int(100000)
intentos=3
print("Buenos dias, inserte su tarjeta")
clave_invalida=True
usuario=int(input("ingrese numero de usuario"))
if usuario==10334151:
   clave=input("Ingrese Clave:")
   while clave_invalida and intentos>1:
            if clave=="1803":
                clave_invalida=False
                print("clave correcta")
                dinero=int(input("Cuanto dinero desea retirar?"))
                if  int(dinero)> (100000):
                    print("saldo insuficiente")
                elif int(dinero)>(1000000):
                     print("cajero no cuenta con esa cantidad de dinero")
                else:saldo_cuenta=Saldo_cuenta-dinero
                saldo_cajero=Saldo_cajero-dinero
                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero)
                break
            else:clave_invalida=True
            intentos=intentos-1
            print("clave incorrecta, intentelo nuevamente")
            clave= input("Ingrese Clave")        
else:
    print("usuario inexistente")