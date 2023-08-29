ingreso=int(input("Señale su ingreso"))
nacimiento=int(input("Señale su año de nacimiento"))
hijos=int(input("¿Cuántos hijos tiene?"))
banco=int(input("¿Hace cuántos años pertenece al banco?"))
estadoc=str(input("¿Estás soltero(S) o casado(C)?"))
vive=str(input("¿Vives en campo(R) o ciudad(U)?"))
edad=(2017-nacimiento)
if   (banco>10 and hijos>=2):
        print("APROBADO")
elif (estadoc==str("C") and hijos>3 and 45<edad<55):
        print("APROBADO")
elif (ingreso>2500000 and estadoc==str("S") and vive==str("U")):
        print("APROBADO")
elif (ingreso>3500000 and banco>5):
        print("APROBADO")
elif (vive==("R") and estadoc==("C") and hijos<2):
        print("APROBADO")
else:
        print("RECHAZADO")
