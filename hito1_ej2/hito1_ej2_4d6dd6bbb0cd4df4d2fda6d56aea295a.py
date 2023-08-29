#Contestador de celular
numerotelefono=int(input("Ingrese número telefónico: "))
hora=int(input("Ingrese hora de la llamada: "))
numi=str(numerotelefono)
#Si la llamada ocurre entre 00:00 y 07:00, la contestas por emergencia
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular

if hora>=0 and hora<=7:
    print("Resultado: CONTESTAR")
if hora>7 and hora<=14:
    if numerotelefono%10**3==909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
if hora>14 and hora<17:
    print("Resultado: NO CONTESTAR")
if hora>=17 and hora<=19:
    if numi[:3]==str(877):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
if hora>19 and hora<=23:
    print("Resultado: NO CONTESTAR")
    
    