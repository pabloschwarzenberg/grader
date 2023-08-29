#Cajero Automático
#Cajero Automático
Usuario_valido="10334151"
Clave_valida="1803"
Saldo_Cta=100000
Billetes_20=20
Billetes_10=40
Billetes_5=40
Billetes_2=0
Billetes_1=0
Nro_Retiros=Nro_Depositos=0
Saldo_Cajero=1000000
Usuario_valido=input("Introduzca Su usuario:")
Error_Clave=1
Respuesta="S"
while Respuesta=="S" or Respuesta=="s":
    Clave=input("Introduzca Su Clave:")
    if Clave==Clave_valida :
            Monto=int(input("Ingrese el monto a Retirar:"))
            if Monto <= Saldo_Cta :
                    Saldo_Cta-=Monto
                    Saldo_Cajero-=Monto
                    B20=B10=B5=B2=B1=0
                    if Monto >= 20000 :
                            B20 = Monto // 20000
                            Billetes_20-=B20
                    Monto=Monto - B20*20000
                    if Monto >= 10000 :
                            B10 = Monto // 10000
                            Billetes_10-=B10
                    Monto=Monto - B10*10000
                    if Monto >= 5000 :
                            B5 = Monto // 5000
                            Billetes_5-=B5
                    Monto=Monto - B5*5000
                    if Monto >= 2000 :
                            B2 = Monto // 2000
                    Monto=Monto - B2*2000
                    if Monto >= 1000 :
                            B1 = Monto // 1000
                    Monto=Monto - B1*1000
                    print("saldo cuenta="+str(Saldo_Cta))
                    print("saldo cajero="+str(Saldo_Cajero))
                    if B20>0 :
                        print("billetes 20000="+str(B20))
                    if B10>0 :
                        print("billetes 10000="+str(B10))
                    if B5>0 :
                        print("billetes 5000="+str(B5))
                    if B2>0 :
                        print("billetes 2000="+str(B2))
                    if B1>0 :
                        print("billetes 10000="+str(B1))
            else :
                print("monto no permitido")
                Error_Clave=1

            Respuesta=input("Deseas Seguir procesando operaciones bancarias (S/N):")
            if Respuesta=="N" or Respuesta=="n" : break
    else :
        print("clave invalida")
        Error_Clave+=1
    if Error_Clave > 3 :
                  print("tarjeta bloqueada")
                  break
     