#Contestador de celular

n= int(input("Por favor ingresar numero Telefono: "))
f= int(input("Por favor ingresar hora: "))


ultimo = int(str(n)[-3:])

if 909 == ultimo:
    antes_14 = ultimo
    if   7 >= f:
        print("CONTESTAR")

    elif (7 < f)  and (14 >= f):
     
        print("CONTESTAR")

    elif 19 <= f:

        print("NO CONTESTAR")
    

elif 877 == ultimo:
    durante_17_19 = ultimo
    if 7 >= f:
        print("CONTESTAR")
    
    elif (17 < f)  and (19 >= f):
        
        print("CONTESTAR")

    elif 19.1 < f:
        print("NO CONTESTAR")

elif 909 != ultimo:
    if   7 >= f:
        print("CONTESTAR")

    elif (7 < f)  and (14 >= f):
     
        print("NO CONTESTAR")

    elif 19 <= f:

        print("NO CONTESTAR")
   
       
    elif (17 < f)  and (19 >= f):
        
        print("NO CONTESTAR")

    
    