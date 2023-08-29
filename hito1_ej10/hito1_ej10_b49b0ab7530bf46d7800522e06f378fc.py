#Cajero Automático
usuario=10334151
clave_original=1803
saldo_u=100000
saldo_cajero=1000000
intentos=3
A="N"
if __name__ == "__main__":
    Usuario=eval(input("Ingrese su Usuario: "))
if __name__ == "__main__": 
    A1=input("Presione cualquier tecla si desea salir del programa y 'N' para continuar: ")
    if A1==A:
        while intentos>0:
            if __name__ == "__main__": 
                Clave=eval(input("Ingrese la Clave: "))
                intentos=intentos-1
                if Clave==clave_original:
                    print("Bienvendio")
                    if __name__ == "__main__": 
                        monto_retiro=eval(input("Ingrese el monto a retirar: "))
                        if monto_retiro>saldo_u:
                            print("Monto no permitido")
                        elif monto_retiro<saldo_u:
                            saldo_actualizado=saldo_u - monto_retiro
                            saldo_nvcajero=saldo_cajero - monto_retiro
                        print("Saldo cuenta=",saldo_actualizado)
                        print("Saldo cajero=",saldo_nvcajero)
                        break
                elif Clave !=clave_original:
                    print("Clave invalida")
    elif A1!=A:
        print("Usted ha salido del programa")            
if intentos==0:
    print("Tarjeta bloqueada")

    
    
    