#Contestador de celular
n = eval(input("ingrese numero de 8 cifras:"))

hora = eval(input("ingrese hora entre 0-23:"))

llamada = str(n)

llamada1 = llamada[5:8]

llamada2 = llamada[0:3]

if (hora >= 0) and (hora <=7): 
    print ("CONTESTAR")

elif (hora<14) and (llamada1!="909"):
    print ("NO CONTESTAR")
    
elif (hora<14)and (llamada1=="909"):
    print ("CONTESTAR")
    
elif (hora>=14) and (hora<17):
    print ("NO CONTESTAR")

elif (hora>=17)and(hora<=19)and(llamada2!="877"):
    print ("CONTESTAR")

elif (hora>=17)and(hora<=19)and(llamada2=="877"):
    print ("NO CONTESTAR")

elif (hora>19):
    print ("NO CONTESTAR")
    
