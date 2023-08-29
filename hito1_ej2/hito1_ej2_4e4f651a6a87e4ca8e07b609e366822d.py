#Contestador de celular
n=input("Ingrese Numero Telefónico:")
m=int(input("Ingrese hora de la llamada:"))
if (0<=m<=7):
    print("CONTESTAR")

else:
    if(7<m<=14):
        o = n[5]
        p = n[6]
        q = n[7]
        if (o=="9" and p=="0" and q=="9"):
            print("CONTESTAR")
        else:
                print("NO CONTESTAR")
    else:

             if (14<m<=17):
                 print("NO CONTESTAR")
if(17<m<=19):
    r = n[0]
    s = n[1]
    t = n[2]
    if(r=="8" and s=="7" and t=="7"):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
        
elif (19<m<=23):
    print("NO CONTESTAR")
                    