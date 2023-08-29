numerotelefono=int(input("Ingrese numero telefonico "))
hora=int(input("Ingrese hora de la llamada"))
if(hora==0 or hora==1 or hora==2 or hora==3 or hora==4 or hora==5 or hora==6 or hora==7):
    print("CONTESTAR")
elif (hora == 8 or hora == 9 or hora == 10 or hora == 11 or hora == 12 or hora == 13 or hora == 14) and (numerotelefono % 1000 == 909):
    print("CONTESTAR")
elif(hora==8 or hora==9 or hora==10 or hora==11 or hora==12 or hora==13 or hora==14):
    print("NO CONTESTAR")
elif(hora==15 or hora==16):
    print("NO CONTESTAR")
elif (hora == 17 or hora == 18 or hora == 19) and (numerotelefono // 100000 == 877):
    print("NO CONTESTAR")
elif(hora==17 or hora==18 or hora==19):
    print("CONTESTAR")
elif(hora==20 or hora==21 or hora==22 or hora==23 or hora==24):
    print("NO CONTESTAR")