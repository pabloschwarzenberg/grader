#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
numero=str(numero)
b=numero[len(numero)-3:len(numero)]
c=numero[0:3]
hora=int(input("Ingrese hora de la llamada: "))
if len(numero)==8:
    if hora>=0 and hora<=7:
        print("Resultado: CONTESTAR")
    elif hora<14:
        if b==str(909):
            print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
    elif hora>=17 and hora<=19:
        if c==str(877):
            print("Resultado: NO CONTESTAR")
        else:
            print("Resultado: CONTESTAR")
    elif hora>=19:
        print("Resultado: NO CONTESTAR")      