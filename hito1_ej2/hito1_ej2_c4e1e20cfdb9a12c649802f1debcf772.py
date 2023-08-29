#Contestador de celular
    
nro=int(input())
hora=int(input())

if  0<=hora<=7:
    print("CONTESTAR")

elif 7<hora<14:
        if(nro-(nro-909))==909:
           print("CONTESTAR")
        else:
           print("NO CONTESTAR")
elif 17<=hora<=19:
        if(nro-(nro-877))==877:
           print("NO CONTESTAR")
        else:
           print("CONTESTAR")

elif 19<hora:
           print("NO CONTESTAR")
