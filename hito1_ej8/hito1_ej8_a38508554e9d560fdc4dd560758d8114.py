num = (input("Ingrese un numero :"))

Contador = len(str(num))
if Contador==4:
    Mil = num[0:1]
    Cen = num[1:2]
    Den = num[2:3]
    Uni = num[3:4]
    print (Mil+"M+"+Cen+"C+"+Den+"D+"+Uni+"U")    
elif Contador==3:
    Cen = num[0:1]
    Den = num[1:2]
    Uni = num[2:3]
    print (Cen+"C+"+Den+"D+"+Uni+"U")
elif Contador==2:
    Den = num[0:1]
    Uni = num[1:2]
    print (Den+"D+"+Uni+"U")
elif Contador==1:
    Uni = num[0:1]
    print (Uni+"U")
