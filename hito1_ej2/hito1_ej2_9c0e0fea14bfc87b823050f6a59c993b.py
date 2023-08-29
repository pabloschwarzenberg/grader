x = int(input("Ingrese numero telefonico de 8 cifras: "))
y = int(input("Ingrese hora de la llamada: "))


k= str(x)
p=k[5]
u=k[6]
h=k[7]

if(p==str(9)) and (u==str(0)) and (h==str(9)):
 print("resultado: Contestar")


k= str(x)
p=k[0]
u=k[1]
h=k[2]

if(p==str(8)) and (u==str(7)) and (h==str(7)):
 print("resultado: No Contestar")


#de 00:00 a 07:00 hrs
else:
    if(y==0 or y==1 or y==2 or y==3 or y==4 or y==5 or y==6 or y==7):
     print("Resultado: Contestar")

#de 08:00 a 13:00 hrs
    else:
        if(y==8 or y==9 or y==10 or y==11 or y==12 or y==13):
         print((p==str(9)) and (u==str(0)) and (h==str(9)) and "Resultado: No contestar")

#de 17:00 a 19:00 hrs 
        else:
            if(y==17 or y==18 or y==19):
             print("Resultado: Contestar")

#de 20:00 a 23:00 hrs
            else:
                if(y==20 or y==21 or y==22 or y==23):
                 print("Resultado: No contestar") 