print("programa contestador de llamadas ")

num_t = str(input("ingrese numero telefonico : "))
hora = int(input ("ingrese hora de llamada : " ))

extraccion = num_t[5:9]

tra_2 = num_t[0:3]

 
if 0<= hora <=7 :
    print("Resultado: CONTESTAR" )

elif 7 < hora < 14:
    if extraccion  == "909":
        print("Resultado: CONTESTAR" )

    else:
        print("resultado: NO CONTESTAR" )
elif hora > 17 and hora < 19 :
    if tra_2 == "877" :
        print("Resultado : NO CONTESTAR")
    else:    
        print("Resultado: CONTESTAR" )

   

elif hora >= 19:
    print("Resultado : NO CONTESTAR")
    
    

