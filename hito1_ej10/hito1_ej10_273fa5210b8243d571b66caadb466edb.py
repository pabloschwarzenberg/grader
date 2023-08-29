cajero = 1000000
cuenta = 100000

while True:
    i=0
    while i < 3:
      u = int(input("Ingrese su número de cuenta: "))
      v = int(input("Ingrese su clave: "))
      if u != 10334151 or v != 1803:
        print("Clave inválida")
        i = i + 1
      else:
        while True:
            m = int(input("Ingrese el monto a retirar: "))
            if m > cuenta:
                print("Monto no permitido")
            else:
                cajero = cajero - m
                cuenta = cuenta - m
                i = 4
                print("Saldo cuenta=", cuenta)
                print("Saldo cajero=", cajero)
                break


    if i == 3:
        print("Tarjeta bloqueada")
        break
    else:
        s = str(input("¿Desea salir? Presione algo distinto de N"))
        w=str("N")
        o=str("n")

        if s!=w and s!=o:
            break