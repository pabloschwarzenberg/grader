intento=0
n=True
while n:
    while intento<3:
        saldoU= 100000
        saldoC = 1000000
    
        usuario=input("ingrese usuario:  ")
        clave = input("ingrese clave:  ")
        if usuario == "10334151" and clave == "1803":
          print("ingreso correcto")
          m = int(input("monto a retirar:  "))
        else:
            print('ingreso incorrecto')
            break  
    if intento=intento+1:
    print("tarjeta bloqueada")


    else:
    m<=saldoC:
        saldoU=saldoU-m
        saldoC=saldoC-m                     
        print("Retiro Exitoso!!!")
        print("saldo actual del cajero:", saldoC);
        print("su saldo actual en la cuenta es:",saldoU)
         
      m<=saldoU:
        saldoC=saldoC-m
        saldoU=saldoU-m
        print("Retiro Exitoso!!!")
        print("saldo actual del cajero:", saldoC)
        print("su saldo actual en la cuenta es:",saldoU)
        
        print("MONTO NO VALIDO")    