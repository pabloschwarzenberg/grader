#contestador automatico

n = int(input("ingrese numero de telefono: "))
h = int(input("ingrese hora de llamada: "))

#entre 0 y 7 se contesta
#antes de los 14 no se contesta, excepto si nt termina en 909
#contesta entre 17 y 19, excepto numero q comienza por 877
#dsps de las 19 no se contesta

#desarrollo

if 0 <= h <= 7:
    print("CONTESTAR")
    

elif n == 77389909 :
        print("CONTESTAR")


elif 17 <= h <= 19:
    print("CONTESTAR")
    if n != 87700000:
        print("NO CONTESTAR")

elif 14 < h < 17:
        print("NO CONTESTAR")
    

elif 19 < h < 23:
    print("NO CONTESTAR")
    
elif h < 14:
    print("NO CONTESTAR")

    