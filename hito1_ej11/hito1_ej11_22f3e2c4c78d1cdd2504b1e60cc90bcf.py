#Cajero Automático
usuario_valido = "10334151"
clave_valida = "1803"
saldo_usuario = 100000
saldo_cajero = 1000000


intentos_fallidos = 0


billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
   
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

  
    if usuario == usuario_valido and clave == clave_valida:
      
        intentos_fallidos = 0

       
        monto = float(input("Ingrese el monto a retirar: "))

     
        if monto <= saldo_usuario:
          
            billetes_20000_retirados = min(billetes_20000, int(monto / 20000))
            billetes_10000_retirados = min(billetes_10000, int((monto - billetes_20000_retirados * 20000) / 10000))
            billetes_5000_retirados = min(billetes_5000, int((monto - billetes_20000_retirados * 20000 - billetes_10000_retirados * 10000) / 5000))

         
            billetes_20000 -= billetes_20000_retirados
            billetes_10000 -= billetes_10000_retirados
            billetes_5000 -= billetes_5000_retirados

          
            saldo_usuario -= monto
            saldo_cajero -= monto

           
            print("saldo cuenta =", saldo_usuario)
            print("saldo cajero =", saldo_cajero)

            print("billetes 20000 =", billetes_20000_retirados)
            print("billetes 10000 =", billetes_10000_retirados)
            print("billetes 5000 =", billetes_5000_retirados)
        else:
            print("Monto no permitido")
    else:
        
        intentos_fallidos += 1

        
        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave inválida")


    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break      