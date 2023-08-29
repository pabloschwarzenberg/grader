
celular = input("Ingresar numero telefono: ")
hora = input("Ingresar hora de llamada: ")

largocelular = celular
len(largocelular)
#print(len(largocelular))

largocelular = int(len(largocelular))
hora = int(hora)
#print("Largo de Celular: ", largocelular)
#print("Numero de Celular: ", celular)
#print("Hora: ", hora)

siTerminaEn = "909"
siComienzaEn = "877"

x = celular
#print(x[:3])
x = x[:3]

y = celular
#print(y[5:])
y =  y[5:]

if largocelular == 8:
    #print("dentro")
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