#Contestador de celular
numerocel=input()
a=int(numerocel[0])
b=int(numerocel[1])
c=int(numerocel[2])
f=int(numerocel[5])
g=int(numerocel[6])
h=int(numerocel[7])
hora=int(input())
if 0<hora<7:
    print("CONTESTAR")
else:
    if 7<hora<14 and f==9 and g==0 and h==9:
        print("CONTESTAR")
    else:
        if 7<hora<14 :
            print("NO CONTESTAR")
        else:
            if 14<hora<17:
                print("NO CONTESTAR")
            else:
                if 17>hora>19:
                    print("CONTESTAR")
                else:
                    if 17>hora>19 and a==8 and b==7 and c==7:
                        print("NO CONTESTAR")
                    else:
                        print("NO CONTESTAR")