n=int(input("ingrese numero telefonico: "))
h=int(input("ingrese hora de llamada "))



ultimos3digitos=n%1000

primero3digitos=(n%1000000000)
primeros33digitos=(primero3digitos//1000000)



if h>0 and h<7:
    print("CONTESTAR")


    #sin expecion
elif h<14 and ultimos3digitos!=909:
    print("NO CONTESTAR")

   # con expecion
elif h<14 and ultimos3digitos==909:
    print("CONTESTAR")


elif h>17 and h<19:
    print("NO CONTESTAR")

elif primeros33digitos==877:
    print("CONTESTAR")

elif h>19:
    print("NO CONTESTAR ")
