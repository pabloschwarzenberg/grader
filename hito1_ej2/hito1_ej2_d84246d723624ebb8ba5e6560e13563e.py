#Contestador de celular
celular = input("Ingresar numero telefono: ")
hora = input("Ingresar hora de llamada: ")

largocelular = celular
len(largocelular)


largocelular = int(len(largocelular))
hora = int(hora)


siTerminaEn = "909"
siComienzaEn = "877"

x = celular

x = x[:3]

y = celular

y = y[5:]

if largocelular == 8:
  
    if hora == 0 or hora <= 7:
        print("Resultado: CONTESTAR")
    elif hora > 7 or hora <= 14:
        if siTerminaEn == y:
            print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
    elif hora >= 17 or hora <= 19:
        if siComienzaEn == x:
            print("Resultado: NO CONTESTAR")
        else:
            print("Resultado: CONTESTAR")
    elif hora > 19:
        print("Resultado: NO CONTESTAR")
else:
    print("debe ingresar un celular de largo 8")     