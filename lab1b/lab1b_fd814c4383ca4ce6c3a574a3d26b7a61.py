#Heladas
iniciar=input("¿Quiere medir la temperatura?")
while iniciar!="si":
    print("Que tenga un buen día")
    break
else:
    x=int(input("temperatura 1:"))
    y=int(input("temperatura 2:"))
    z=int(input("temperatura 3:"))
    if x<=0 or y<=0 or z<=0:
        print("encendido")
        print("encendido")
        print("encendido")
    else:
        if x>5:
            print("apagado")
        else:
            print("encendido")
        if y>5:
            print("apagado")
        else:
            print("encendido")
        if z>5:
            print("apagado")
        else:
            print("encendido")
    x=int(input("temperatura 1:"))
    y=int(input("temperatura 2:"))
    z=int(input("temperatura 3:"))
      