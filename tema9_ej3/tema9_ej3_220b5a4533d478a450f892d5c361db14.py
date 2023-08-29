def decodificar(ms):
    L= []
    a= ms.replace("'", "")
    a= ms.replace(",", " ")
    x1= a[0:8] #9 coma
    x2= a[9:17]#18 coma
    x3= a[18:26]#27 coma
    x4= a[27:35]#36 fin
    Decodificador1= int(str(x1), int(2))
    Decodificador2= int(str(x2), int(2))
    Decodificador3= int(str(x3), int(2))
    Decodificador4= int(str(x4), int(2))
    tranf1= chr(Decodificador1)
    tranf2= chr(Decodificador2)
    tranf3= chr(Decodificador3)
    tranf4= chr(Decodificador4)
    L.append(tranf1)
    L.append(tranf2)
    L.append(tranf3)
    L.append(tranf4)
    j= str(L)
    y= j.replace("[","")
    y= y.replace("]","")
    y= y.replace(",","")
    y= y.replace("''", "")
    y= y.replace(" ","")
    y= y.replace("'", "")
    return (y)


    ms=decodificar("01101000,01101111,01101100,01100001")
    print(ms)
         