p1 = [1, "Pokemon X para Nintendo 3DS", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58]
p4 = [4, "PlayStation 4", 348]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]
p1 = str(p1)
p2 = str(p2)
p3 = str(p3)
p4 = str(p4)
p5 = str(p5)
ptos = [p1, p2, p3, p4, p5]
carro = []

while True:

    kill = str(input("Ingrese accion: "))

    if (kill != "ver" and kill != "checkout"):
        #es necesario llamar a la función split para separar en dos partes el texto
        #los productos se ingresan desde el 1 en adelante
        kill = kill.split(",")
        prod = int(kill[0])
        cant = int(kill[1])


    #for x in range(cant):
        #los indices de los productos en la lista parten en 0, pero se ingresan desde 1
        carro.append(cant*ptos[prod-1])

    if (kill == "ver"):

        print(carro)

    elif (kill == "checkout"):
        
        carro = str(carro)
        carro.split("][")
        z = carro.count(p1)
        e = carro.count(p2)
        f = carro.count(p3)
        r = carro.count(p4)
        qa = carro.count(p5)
        w1 = [1, "Pokemon X para Nintendo 3DS", 33.77]
        w2 = [2, "Nintendo 3DS XL", 203]
        w3 = [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58]
        w4 = [4, "PlayStation 4", 348]
        w5 = [5, "FIFA 16, PlayStation 4", 51.19]
        
        
        cta=(z*w1[2]+e*w2[2]+f*w3[2]+r*w4[2]+qa*w5[2])
        print (z,e,f,r,qa)
        print(w1[2],w2[2],w3[2],w4[2],w5[2])
        if(z >0 and e>0 and f>0):

            
            cuenta = 0.8*cta

            if(r>0 and qa>0):
                
                cuenta = 0.65*cta

        elif(r>0 and qa>0):

            cuenta = 0.85*cta

        else:

            cuenta = cta
                
            

        cuenta = round(cuenta, 1)
        print(cuenta)
        print(prod,cant)

        break