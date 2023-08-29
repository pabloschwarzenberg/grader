#Cajero Automático
bille20Dis = 20
bille10Dis = 40
bille5Dis = 40
bille20ent = 0
bille10ent = 0
bille5ent = 0
saldoCaj = 1000000
monto = 0
giro = 0
bandeja = "b20"
pedirGiro = True
#Variables ejercicio anterior
intentos = 0
usuario = ""
clave = ""
cuentaInicio = 100000
comprobante = True

#Valido el usuario, la clave y los intentos
while intentos < 3:
    usuario = input("\n¿Usuario?: ")
    clave = input("¿Clave?: ")
    
    if usuario == "10334151" and clave == "1803":  
        break
    else:
        print("\nclave invalida...")  

        intentos += 1
    
    if intentos == 3:
        print("\nTarjeta bloqueada")    
        pedirGiro = False        
        comprobante = False              

#Fin validacion usuario

#Valido que el monto del giro sea correcto 
while pedirGiro:
    giro = int(input("Ingrese giro: "))

    if giro > cuentaInicio:
        print("Monto no permitido. Vuelva a ingresar monto a retirar")
    elif giro > saldoCaj:
        print("El monto es mayor que la disponibilidad del cajero. Porfavor ingrese de nuevo.")
    elif giro % 5000 > 0:
        print("Este cajero solo entrega multiplos de $5000. Porfavor ingrese nuevamente.")
    else:
        pedirGiro = False

#Procede a la entrega de dinero
while monto < giro:

    #Valido si el billete que entrego satisface el monto
    #Descarto bandeja de 20
    if (monto + 20000) > giro or bille20Dis == 0:
        bandeja = "b10"

    #Descarto bandeja de 10
    if (monto + 10000) > giro or bille10Dis == 0:
        bandeja = "b5"

    #Nose de que bandeja sacar plata
    if bandeja == "b20":
        bille20ent += 1
        bille20Dis -= 1
        monto = monto + 20000
    elif bandeja == "b10":
        bille10ent += 1
        bille10Dis -= 1
        monto = monto + 10000
    elif bandeja == "b5":
        bille5ent += 1
        bille5Dis -= 1
        monto = monto + 5000
    


if comprobante == True:
    #print("Monto: ", monto, "Giro: ", giro)
    #print("billetes 20000:", bille20ent, " bille10:", bille10ent, " bille5:", bille5ent)
    print("billetes 20000=", bille20ent)
    print("billetes 10000=", bille10ent)
    print("billetes 5000=", bille5ent)
    
    
    cuentaInicio -= giro
    saldoCaj -= giro
    print("Saldo cuenta=", cuentaInicio, "saldo cajero=", saldoCaj)