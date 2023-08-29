#Cajero Automático
usuario = 10334151
clave = 1803
saldocajero = 1000000
saldousuario = 100000
a = 0
i = 1
while i<=3 and i==1: 
    while a == 0:
        a = int(input("Ingresa usuario: "))
        if a == usuario:
            b = int(input("Clave: "))
            if b == clave:
                sacar=int(input("Cuanto retiraras: "))
                if sacar < saldousuario:
                    x = saldousuario-sacar
                    y = saldocajero-sacar
                    print("saldo cuenta=", x)
                    print("saldo cajero=", y)
     
                    
            while b != clave:
                print("clave invalida")
                b = int(input("Clave: "))
                i = i+1
                if i ==3:
                    print("tarjeta bloqueada")
                    break
    break                    