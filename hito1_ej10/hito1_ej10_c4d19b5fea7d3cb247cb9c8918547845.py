saldo = 1000000
saldop = 100000
usu = int(input("Ingrese usuario:"))

i = 0

while i<3:
    i = i+1
    clave = int(input("Ingrese clave: "))

    if(usu == 10334151 and clave == 1803):
        while True:
            mont = input("Monto a retirar:")
            if mont.isdigit():
                mont = int(mont)

                if (mont > saldo):
                    print("MONTO NO PERMITIDO")
                    continue

                if (mont > saldop):
                    print("MONTO NO PERMITIDO")
                    continue

                elif(mont<saldo or mont<saldop):
                    saldo = (saldo-mont)
                    saldop = (saldop - mont)
                    print("Saldo cuenta=", saldop)
                    print("Saldo cajero=", saldo)
                    cont = input("Desea continuar?")
                    break
    if (cont.isalpha() and cont != "n" or cont != "N"):
        print ("Adios")
        break    
                  
    elif (clave<1803 or clave>1803):
        print("CLAVE INCORRECTA")
        continue
         

if (i >= 3):
    print("TARJETA BLOQUEADA")
    exit(0)










    

    











    
