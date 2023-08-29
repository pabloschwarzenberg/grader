#Cajero Automático
user= "10334151"
clave= "1803"
saldo= int(100000)
intentos=0
usuario=0
cajero=int(1000000)
import sys
retiro=0

print("Cajero")
while intentos==0:
    n= input("Ingrese usuario")
    if n == user:
        print("Ingrese Registrado")
        intentos=intentos+3
        while intentos>0:
            if intentos>0:
                c= input("Ingrese Clave")
                if c==clave:
                    print("Clave correcta")
                    print("Ingresando a la cuenta")
                    print("Saldo disponible",saldo)
                    while True:
                        resta=int(input("Monto a retirar:"))
                        if resta>saldo:
                            print("Saldo Insuficiente")

                        else:
                            total=saldo-resta
                            cajero2=cajero-resta
                            print("Su nuevo saldo es:", total)
                            print("Al cajero le queda", cajero2)
                            print("Gracias por operar")
                            intentos=-8
                            break
                        
                        
                
                

                else:
                    print("Clave incorrecta")
                    intentos=intentos-1
        else:
            if intentos==0:
                print("intentos superados")

            elif intentos==-8:
                break
                

        
        
    else:
        print("El usuario es icorrecto")      