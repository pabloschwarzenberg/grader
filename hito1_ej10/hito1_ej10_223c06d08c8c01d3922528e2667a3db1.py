usuariobase = 10334151
clavebase = 1803
saldocaje = 1000000
cuentadi = 100000
inte = 0
print("El cajero tiene $" , saldocaje)
while inte < 3:
            clave = int(input("Clave "))
            if clave == clavebase:
                print("El cajero tiene $" , saldocaje)
                print("Saldo de la cuenta $", cuentadi)
                retiro = int(input("Saldo a retirar "))
                if (retiro <= saldocaje) and (retiro <= cuentadi):
                    cuentadi = cuentadi - retiro
                    saldocaje = saldocaje - retiro
                    print("saldo cuenta=" + str(cuentadi))
                    print("saldo cajero=" + str(saldocaje))
                    break
                else:
                    print("monto no permitido")
                    break
                
            else:
                inte = inte + 1
                print(inte, " intentos fallidos de 3")
                if inte == 3:
                    print("Tarjeta bloqueada")
                    break
