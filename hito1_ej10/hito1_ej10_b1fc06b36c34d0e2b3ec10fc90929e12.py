saldocajero = 1000000
saldocuenta = 100000
contador     = 0
contador2    = 0
usuario      = int(input("ingrese usuario : "))
clave        = int(input("ingrese clave : "))
if __name__ == "__main__":
    while contador<2 and contador2<2:
     if usuario == 1 and clave ==2:

       retirar = int(input("cual es el monto que desea retirar: "))
       if retirar < saldocajero:
         saldocuenta-=retirar
         saldocajero-=retirar
         print("saldo cuenta=",saldocuenta)
         print("saldo cajero=",saldocajero)
         con = str(input("continuar ? F no T si:"))
         if con == "F":
                 print("gracias")
                 contador2+=2
         if con == "T":
                     retirar = int(input("cual es el monto que desea retirar: "))
       if retirar>saldocajero:
        print("sin saldo suficiente: ")
        retirar =int(input("cual es el monto que desea retirar: "))

     else:
            contador+=1
            print("Usuario y/o clave incorrectos. Lleva",contador,"intento(s) fallidos. Al tercer intento Bloquearemos la tarjeta")
            print (contador)
            usuario = int(input("ingrese usuario : "))
            clave = int(input("ingrese clave : "))
     if contador ==2:
         print("Tarjeta Bloqueada")
         print("Tarjeta Bloqueada")