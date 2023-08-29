#Descomponer un número
n = str(input("ingrese el numero:"))

c = len(str(n))  

#4 digitos

if c == 4:

    a = n[0] + "M +"
    b = n[1] + "C +"
    c = n[2] + "D +"
    d = n[3] + "U"
        
    print (a,b,c,d)

#3 digitos

if c == 3:

    a = n[0] + "C +"
    b = n[1] + "D +"
    c = n[2] + "U"

    print (a,b,c)

#2 digitos

if c == 2:

    a = n[0] + "D +"
    b = n[1] + "U"

    print (a,b)

#1 digitos

if c == 1:

    a = n[0] + "U"

    print (a)