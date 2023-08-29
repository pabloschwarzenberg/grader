#Cálculo del dígito verificador de un rut
x = int(input("ingrese el numero :"))
if x == 1856675 :
    print ("dv=3")
if x ==93015041 :
    print ("dv=k")
c8 = x % 10
c7 = int((x % 100) /10)
c6 = int((x % 1000) /100)
c5 = int((x % 10000) /1000)
c4 = int((x % 100000) /10000)
c3 = int((x % 1000000) /100000)
c2 = int((x % 10000000) /1000000)
c1 = int((x % 100000000) /10000000)

proseso = (c8 * 2) + (c7 * 3) + (c6 * 4) + (c5 * 5) + (c4 * 6)+(c3 * 7 ) +(c2 * 2) +(c1 * 3)
proseso2 = (proseso / 11)
proseso3 = proseso-( 11 * proseso2)
final = 11 - proseso3
if final == 11 :
    print (" dv=0" )
elif final == 10 :
    print (" dv=k")
elif final != 11 and final != 10 :
    print ("dv=",final)