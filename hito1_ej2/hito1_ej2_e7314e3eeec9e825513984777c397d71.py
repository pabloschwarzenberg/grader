#Contestador de celular
a=int(input("Inserte numero telefónico (8 numeros): "))
b=int(input("Inserte hora de la llamada: "))
c=(((((a%10000000)%1000000)%100000)%10000)%1000)
f=(a//100000)
x=f

if 0<=b<=7:
    print("CONTESTAR")
else:
    if 7<b<14 and c==909:
        print("CONTESTAR")
    else:
        if 7<b<14:
            print("NO CONTESTAR")
        else:
            if 17<=b<=19 and x!=877:
                print("CONTESTAR")
            else:
                if 17<=b<=19 and x==877:
                    print("NO CONTESTAR")
                else:
                    if b>19:
                        print("NO CONTESTAR")     