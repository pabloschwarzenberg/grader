print("Bienvenido al contestador de celulares, por favor ingrese a continuación el numero entrante y la hora de la llamada: ")
#n= numero  entrante
#h= hora de la llamada
n=input("Ingrese el número telefónico: ")
h=int(input("Ingrese la hora de la llamada: "))
if 0<=h<=23:
    if len(n)==8:
        if 0<=h<=7:
            print("CONTESTAR")
        elif 7<=h<14 and 100*int(n[5])+10*int(n[6])+int(n[7])==909:
            print("CONTESTAR")
            if 17<=h<=19 and 100*int(n[0])+10*int(n[1])+int(n[2])==877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        elif h>19:
            print("NO CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        print("Compruebe el número de telefono")
else:
    print("Compruebe la hora")


      