def decodificar(msj_ej):
    lista = []
    x= msj_ej.replace("'", "")
    x= msj_ej.replace(",", " ")
    a1= x[0:8] #9 coma
    a2= x[9:17]#18 coma
    a3= x[18:26]#27 coma
    a4= x[27:35]#36 fin
    d1= int(str(a1), int(2))
    d2= int(str(a2), int(2))
    d3= int(str(a3), int(2))
    d4= int(str(a4), int(2))
    l1= chr(d1)
    l2= chr(d2)
    l3= chr(d3)
    l4= chr(d4)
    lista.append(l1)
    lista.append(l2)
    lista.append(l3)
    lista.append(l4)
    y= str(lista)
    z= y.replace("[","")
    z= z.replace("]","")
    z= z.replace(",","")
    z= z.replace("''", "")
    z= z.replace(" ","")
    z= z.replace("'", "")
    return (z)

if "_name_" == "_main_":
    msj_ej = decodificar("01101000,01101111,01101100,01100001")
    print(msj_ej)
