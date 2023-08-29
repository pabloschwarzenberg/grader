n=str(input("rut: "))
if int(n) > 9999999:
        
    n1 = int(n[7:8]) * 2
    n2 = int(n[6:7]) * 3
    n3 = int(n[5:6]) * 4
    n4 = int(n[4:5]) * 5
    n5 = int(n[3:4]) * 6
    n6 = int(n[2:3]) * 7
    n7 = int(n[1:2]) * 2
    n8 = int(n[0:1]) * 3

    producto = int((n1+n2+n3+n4+n5+n6+n7+n8))
    entera = int(producto / 11)
    division = int(producto) - (11*(entera))
    dv = 11 - (division)
    if dv == 10:
        DV="K"
    elif dv == 11:
        DV = 0
    else:
        DV = dv

    
elif int(n) < 9999999:
        
    n1 = int(n[6:7]) * 2
    n2 = int(n[5:6]) * 3
    n3 = int(n[4:5]) * 4
    n4 = int(n[3:4]) * 5
    n5 = int(n[2:3]) * 6
    n6 = int(n[1:2]) * 7
    n7 = int(n[0:1]) * 2

    producto = int((n1+n2+n3+n4+n5+n6+n7))
    entera = int(producto / 11)
    division = int(producto) - (11*(entera))
    dv = 11 - (division)

    if dv == 10:
        DV="K"
    elif dv == 11:
        DV = 0
    else:
        DV = dv
print ("dv= ",DV)
    

    
    
