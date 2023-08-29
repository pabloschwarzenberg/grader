#Cajero Automático
usuarioguardado = "10334151"
contrasenaguardada ="1803"
montoinicialguardado = 100000
saldocajero = 1000000
ntbill20k = 20
ntbill10k = 40
ntbill5k = 40
usuarioentrada = ""
contrasenaentrada = ""
intentos = 3
while usuarioentrada != usuarioguardado:
    usuarioentrada = input("Ingrese su usuario: ")
    if usuarioentrada == usuarioguardado:
        break
        print("Usuario no encontrado, reintente denuevo")
               
while intentos > 0:
    contrasenaentrada = input("Ingrese su contraseña, tiene " + str(intentos) + " intentos: " )
    if contrasenaentrada == contrasenaguardada:
        break
    
    intentos -= 1
    if intentos == 0:
        print("tarjeta bloqueada")
        break

if intentos != 0:
    while True:
        print("¿Cuanto monto desea retirar? , actualmente usted tiene: " , str(montoinicialguardado))
        montoretiro = int(input("Monto a retirar: "))
        if (montoinicialguardado - montoretiro) < 0 and (montoretiro < 0):
            print("Monto Invalido , porfavor reintente denuevo")
        
        if (montoinicialguardado - montoretiro) >= 0 and (montoretiro >= 0):
            montoinicialguardado -= montoretiro
            saldocajero -= montoretiro
            print("saldo cuenta=" , str(montoinicialguardado))
            print("saldocajero=" , str(saldocajero))
            nbilletes20k = montoretiro // 20000
            montoretiro %= 20000
            nbilletes10k = montoretiro // 10000
            montoretiro %= 10000
            nbilletes5k = montoretiro // 5000
            #Disminucion de billetes totales
            ntbill20k -= nbilletes20k
            ntbill10k -= nbilletes10k
            ntbill5k -= nbilletes5k
            #Termina la cantidad de billetes totales
            print("billetes 20000=",str(nbilletes20k))
            print("billetes 10000=",str(nbilletes10k))
            print("billetes 5000=",str(nbilletes5k))
            break
   