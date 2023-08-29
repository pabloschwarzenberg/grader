#Contestador de celular
q = 1

while q == 1:
    x = str(input("Ingrese el numero de llamada --> "))
    print("El numero es: ", x)  
    z = str(x)
    
    if len(x) == 8:
        
        y = int(input("Ingrese la hora a la cual se llama --> "))
        print("La hora a la que se llama es:",y)
        
        
        if (y < 8):
            print("CONTESTAR")
            
        if ((y >= 7) and (y <= 14)):
            
            t = str(z[5:8])
            if (z[5:8] == "909"):
                print("CONTESTAR")
            if (z[5:8] != "909"):
                print("NO CONTESTAR")
            
        
        if (y >= 14) and (y <= 16):
            print("NO CONTESTAR, entre 14 y 17 horas")
            
        if (y >= 17) and (y <= 19):
            r = str(z[0:3])
            if (z[0:3] == "877"):
                print("NO CONTESTAR")
            if (z[0:3] != "877"):
                print("CONTESTAR")
            
        if (y >= 19):
            print("NO CONTESTAR")      

        q = q + 1
              
    else:
        print("Vuelva a ingresar el numero")          