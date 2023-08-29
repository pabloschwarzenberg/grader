usuarioEnBD = "10334151"
claveEnBD = "1803"
saldo = 100000
carga50 = 20
carga20 = 40
carga10 = 40
saldo_cajero = (carga50*20000)+(carga20*10000)+(carga10*5000)

usuario = input("Digite usuario: ")
clave = input("Digite contraseña: ")

if (clave==claveEnBD and usuario ==usuarioEnBD):
    retiro = int(input("Monto a retirar:"))
    if(saldo < retiro) and (saldo_cajero > retiro):
        print("Monto no permitido")
    else: saldo = (saldo - retiro) 
    if(saldo < retiro) and (saldo_cajero > retiro):
        print("Monto no permitido")
    else: saldo_cajero = (saldo_cajero - retiro)
    print("saldo cuenta=",saldo)
    print("saldo cajero=",saldo_cajero)
    def sacar_dinero(cantidad):

      global carga50, carga20, carga10

      if cantidad <= 20000 * carga50 + 10000 * carga20 + 5000 * carga10:

        de50 = int(cantidad / 20000)

        cantidad = cantidad % 20000

        if de50 >= carga50: 

          cantidad = cantidad + (de50 - carga50) * 20000

          de50 = carga50

     
        de20 = int(cantidad / 10000)

        cantidad = cantidad % 10000

        if de20 >= carga20: 

          cantidad = cantidad + (de20 - carga20) * 10000

          de20 = carga20
    

        de10 = int(cantidad / 5000)

        cantidad = cantidad % 5000

        if de10 >= carga10: 

          cantidad = cantidad + (de10 - carga10) * 5000

          de10 = carga10 

        if cantidad == 0:

       

          carga50 = carga50 - de50

          carga20 = carga20 - de20

          carga10 = carga10 - de10

          return [de50, de20, de10]

        else: 

          return [0, 0, 0]

      else:

        return [-1, -1, -1]  

    try:
        resultado=sacar_dinero(retiro)

        if resultado==[0,0,0]:

            print ('No hay desglose de billetes para su importe')

        elif resultado==[-1,-1,-1]:

            print ('No hay suficientes billetes')

        else:

            print ('billetes 20000=', resultado[0])

            print ('billetes 10000=', resultado[1])

            print ('billetes 5000=', resultado[2])

    except:

        print ('Importe incorrecto')
else: print("clave invalida")
