#Cajero Automático
      from os import system
system("cls")

saldo_inicial = 1000000  
saldo_usuario = 100000  
intentos_fallidos = 0  

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == "10334151" and clave == "1803":
     while True:
          monto = float(input("Ingrese el monto a retirar: "))
          if monto <= 0:
               print("Monto no permitido.")
          elif monto > saldo_usuario:
               print("Saldo insuficiente.")
          elif monto > saldo_inicial:
               print("El cajero no dispone de suficiente dinero.")
          else:
                saldo_usuario -= monto
                saldo_inicial -= monto
                print(f"Saldo cuenta: {saldo_usuario}")
                print(f"Saldo cajero: {saldo_inicial}")
                break  
                
    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
            break  
    else:
        intentos_fallidos += 1
        print("Clave inválida.")
        
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break  