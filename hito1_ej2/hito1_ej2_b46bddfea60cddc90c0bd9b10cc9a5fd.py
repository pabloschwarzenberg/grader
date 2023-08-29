#Contestador de celular
numTlf=int(input("Ingrese numero telefonico: "))
horaCall=int(input("Ingrese hora de la llamada: "))

rule2 = str(numTlf).endswith("909")
print(rule2)

rule3 = str(numTlf).startswith("877")

if( numTlf<9999999 or numTlf>99999999 ) :
    print("NO CONTESTAR")

elif ( horaCall<0 or horaCall>23 ) :
    print("NO CONTESTAR")

#contestar entre 00 y 7
elif (horaCall>=0 and horaCall<=7 ) :
    print("CONTESTAR")

#no contestar antes de 14
elif(horaCall<14) :
    if(rule2) :
        print("CONTESTAR")
    else :
        print("NO CONTESTAR")

#contestar entre 17 y 19
elif (horaCall>=17 and horaCall<=19 ) :
    if(rule3):
        print("NO CONTESTAR")
    else :
        print("CONTESTAR")

elif (horaCall > 19 ) :
        print("NO CONTESTAR")      