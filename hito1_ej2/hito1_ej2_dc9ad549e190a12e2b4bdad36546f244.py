#Contestador de celular
numTelef=int(input("Ingrese numero telefonico: "))
horalla=int(input("Ingrese hora de la llamada: "))
rule2 = str(numTelef).endswith("909")
print(rule2)
rule3 = str(numTelef).startswith("877")
if( numTelef<9999999 or numTelef>99999999 ) :
    print("NO CONTESTAR")
elif ( horalla<0 or horalla>23 ) :
    print("NO CONTESTAR")
    
#contestar entre 00 y 7
elif (horalla>=0 and horalla<=7 ) :
    print("CONTESTAR")
    
#no contestar antes de 14
elif(horalla<14) :
    if(rule2) :
        print("CONTESTAR")
    else :
        print("NO CONTESTAR")
        
#contestar entre 17 y 19
elif (horalla>=17 and horalla<=19 ) :
    if(rule3):
        print("NO CONTESTAR")
    else :
        print("CONTESTAR")

elif (horalla > 19 ) :
        print("NO CONTESTAR")      