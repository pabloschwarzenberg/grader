#Cajero Automático
usuarioguardado = "10334151"
contrasenaguardada ="1803"
montoinicialguardado = 100000
saldocajero = 1000000
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
            break
   