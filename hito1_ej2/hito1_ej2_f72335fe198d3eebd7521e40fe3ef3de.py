#Contestador de celular

a=int(input("Ingrese un número telefónico de 8 cifras :"))
b=int(input("Ingrese la hora de su llamada (Debe ser un número entre 0 y 23 :"))

if  b<8:
    print("CONTESTAR")

   
elif b>7 and b<15:

    c=str(a)

    c1=c[5:]

    print(c1)

    if c1=="909":

        print("CONTESTAR")
    
    else:

        print("NO CONTESTAR")

elif b>13 and b<17:

    print ("NO CONTESTAR")


if b>16 and b<20:

    c=str(a)

    c1=c[:3]
    
    if c1=="877":

        print("NO CONTESTAR")
    
    else:

        print("CONTESTAR")

if b>19:

    print("NO CONTESTAR")
      