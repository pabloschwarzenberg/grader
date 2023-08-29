#Cajero Automático
SaldoDelCajero = 1000000
SDelUsuario = 100000
print("Bienvenido")
NDeUsuario = int(input("Ingrese su numero de usuario: "))
if(NDeUsuario == 10334151):
    contador = 3
    for i in range(contador):
        clave = int(input("Ingrese su clave: "))
        if(contador != 0 and clave == 1803):
            print("Hola Diego que cuanto necesitas retirar?")
            retiro = int(input())

            if(retiro <= SDelUsuario):
                print("saldo cuenta=", SDelUsuario - retiro, "Saldo cajero=", SaldoDelCajero - retiro)
                break
            else:
                print("monto no permitido")
                break

        else:
            contador = contador - 1
            print("clave invalida")
            if(contador == 0):
                print("tarjeta bloqueada")
                break