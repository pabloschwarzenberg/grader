#Cajero Automático
saldoCajero = 1000000
saldoCliente = 100000

listaBilletes = [20000,10000,5000]

billetes20000 = 20
billetes10000 = 40
billetes5000 = 40

user = input("Ingrese Usuario: ")
clave = input("Ingrese su Clave: ")

if user == '10334151' and clave == '1803':
    monto = int(input("Ingrese el monto a retirar: "))
    saldoCliente = saldoCliente - monto
    saldoCajero = saldoCajero - monto
    print('saldo cuenta=',saldoCliente)
    print('saldo cajero=',saldoCajero)
    for i in listaBilletes:
        if monto >=i:
            queda = monto // i
            #print (queda,i)
            monto = monto % i
            print ("billetes "+str(i) + "=",queda)