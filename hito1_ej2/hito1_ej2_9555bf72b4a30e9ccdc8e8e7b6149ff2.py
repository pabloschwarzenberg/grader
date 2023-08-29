n=int(input("N° Teléfono: "))
h=int(input("Hora de Llamada: "))

if n>99999999 or n<10000000 or h<0 or h>23:         #No sé como considerar números que comiencen en 0
    print("Datos inválidos")
          
else:
    if h<=7:
        print("Contestar")
    elif h<=13:
        if n%1000==909:
            print("Contestar")
        else:
            print("No contestar")
    elif h<=16:
        print("No contestar")
    elif h<=19:
        a=int(n/100000)
        if a==877:
            print("No Contestar")
        else:
            print("Contestar")
    else:
        print("No contestar")
