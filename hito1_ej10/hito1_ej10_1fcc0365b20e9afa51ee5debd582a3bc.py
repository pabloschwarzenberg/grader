
saldo_i=int(input("ingresar saldo inicial:"))
cuenta=int(input("ingresar saldo cuenta:"))
usr=("10334151")
import random

if __name__ == "__main__":
     print("Bienvenido usr:", usr)
         contraseña=input("ingrese contraseña:")

    if contraseña == "1803":
        print("¿cuanto desea retirar?: Monto disponible:", cuenta)
        monto_retirar=int(input("ingrese el monto a retirar:"))
        if monto_retirar <= cuenta:
            print("saldo cuenta=", saldo_i+monto_retirar,", saldo cajero=", cuenta-monto_retirar)
        else:
            print("monto no permitido.")
            
    if contraseña != "1803":
        print("clave invalida, le qudan 2 intentos")
        contraseña=input("ingrese contraseña:")
    if contraseña != "1803":
        print("clave invalida, le qudan 1 intentos")
        contraseña=input("ingrese contraseña:")
    if contraseña != "1803":
        print("Tarjeta bloqueada")