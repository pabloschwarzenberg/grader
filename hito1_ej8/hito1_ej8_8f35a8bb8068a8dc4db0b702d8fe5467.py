numero = input("Ingrese numero: ")

if numero>="1000":

    a = str(numero[:1])
    b = str(numero[1:2])
    c = str(numero[2:3])
    d = str(numero[3:])

    mil = "M"
    cen = "C"
    dec = "D"
    uni = "U"  
 
    uno = (a+mil)
    dos = (b+cen)
    tres = (c+dec)
    cuatro = (d+uni) 

    print(uno,dos,tres,cuatro,sep=" ")

elif "99" < numero < "1000":

    b = str(numero[:1])
    c = str(numero[1:2])
    d = str(numero[2:])
  
    cen = "C"
    dec = "D"
    uni = "U"  

    dos = (b+cen)
    tres = (c+dec)
    cuatro = (d+uni) 

    print(dos,tres,cuatro,sep=" ")

elif "9" < numero < "99":

        c = str(numero[:1])
        d = str(numero[1:])
  
        dec = "D"
        uni = "U"  
 
        tres = (c+dec)
        cuatro = (d+uni) 

        print(tres,cuatro,sep=" ")

elif numero<"10":

            d = str(numero[:])
  
            uni = "U"  
         
            cuatro = (d+uni) 

            print(cuatro,sep=" ")


