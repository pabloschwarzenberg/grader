#Cajero Automático
Saldo_Inicial_Cajero = 1000000
Saldo_Inicial_Cuenta = 100000
Usuario= "10334151"
Clave = "1803"
Intentos_clave = 0
while True:
    In = str(input("Ingreso Usuario:"))
    if In==Usuario:
        if Intentos_clave == 3:
            print("tarjeta bloqueada")
            break
        In_c=str(input("Ingresp clave: "))
        if In_c == Clave:
            In_M = str(input("Ingrese Monto: "))
            if int(In_M) <= Saldo_Inicial_Cuenta:
                print([("saldo cuenta=" + str(Saldo_Inicial_Cuenta - int(In_M))),
                       ("saldo cajero=" + str(Saldo_Inicial_Cajero - int(In_M)))])
            else:
                print("monto no permitido")
                break
        else:
            print("clave invalida")
            Intentos_clave += 1
            continue
    else:
        continue
    
