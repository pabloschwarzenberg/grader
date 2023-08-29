#Descomponer un número
a = 0
while a == 0:
    
    x = input("Introduce el número: ")

    x = int(x)
    t = str(x)

    len(t)
    

    
    if len(t) > 4:
        print("Vuelva a colocar el numero")
    
    else:
        mil = x / 1000
        tmp = x % 1000

        cien = tmp / 100
        tmp = tmp % 100

        diez = tmp / 10
        tmp = tmp % 10

        uno = tmp / 1 
        tmp = tmp % 1

    if len(t) == 1:
        w = str(int(uno))+"U"
        uno = int(uno)
        print(w)
        a = 1
        
    if len(t) == 2:
        w = str(int(diez))+"D+" +str(int(uno))+"U"
        print(w)
        a = 1
        
    if len(t) == 3:
        w = str(int(cien))+"C+" +str(int(diez))+"D+" +str(int(uno))+"U"
        print(w)
        a = 1
        
    if len(t) == 4:
        w = str(int(mil))+"M+" +str(int(cien))+"C+" +str(int(diez))+"D+" +str(int(uno))+"U"
        print(w)
        a = 1
        