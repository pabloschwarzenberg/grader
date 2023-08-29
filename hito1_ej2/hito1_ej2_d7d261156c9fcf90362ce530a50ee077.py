#Contestador de celular
celular=input("Ingrese número telefónico")
hora=int(input("Ingrese hora de llamada"))
a=int(celular[0])
b=int(celular[1])
c=int(celular[2])
d=int(celular[3])
e=int(celular[4])
f=int(celular[5])
g=int(celular[6])
h=int(celular[7])
if hora>=0 and hora<=7:
    print("CONTESTAR")
else:
    if hora>19 and hora<=23:
        print("NO CONTESTAR")
    else:
        if 17<=hora and hora<=19:
            if a==8 and b==7 and c==7:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            if hora<14 and f==9 and g==0 and h==9:
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
      