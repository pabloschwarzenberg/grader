num = int(input("Ingrese el número telefónico de 8 dígitos: "))
hora = int(input("Ingrese la hora de llamada(00:00-24:00 hra): "))

def contestar_llamada():
    if hora >= 0 and hora < 7:
          print("CONTESTAR")
    elif hora < 14 and hora>7:
        if num%1000==909:
           print("CONTESTAR")
    elif hora > 17 and hora < 19:
        if num//100000==877:
            print("NO CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif hora >7 and hora <23:
        print("NO CONTESTAR")
contestar_llamada()
