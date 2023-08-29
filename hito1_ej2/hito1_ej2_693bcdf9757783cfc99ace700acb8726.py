print("contestador de llamadas")
numeros= int(input("ingrese numero telefonico: "))
hora= int(input("ingrese hora de llamada"))



if hora >= 0 and hora<= 7 :
    print ("contstar")
if int(numeros%1000) == int(909) :
        print("contestar")
elif hora >=8 and hora <=14:
    print ("no contestar")
    
if hora >= 17 and hora<=19 :
    print ("contestar")
    if int(numeros/100000) == int(877):
        print ("no contestar")   
    
if hora >=20 and hora <=23:
    print ("no contestar")

print ("fin de programa") 
