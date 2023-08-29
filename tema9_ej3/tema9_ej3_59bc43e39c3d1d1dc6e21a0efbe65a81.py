def decodificar(men):
    li= []
    x= men.replace("'", "")
    x= men.replace(",", " ")
    a1= x[0:8] #9 coma
    a2= x[9:17]#18 coma
    a3= x[18:26]#27 coma
    a4= x[27:35]#36 fin
    de1= int(str(a1), int(2))
    de2= int(str(a2), int(2))
    de3= int(str(a3), int(2))
    de4= int(str(a4), int(2))
    l1= chr(de1)
    l2= chr(de2)
    l3= chr(de3)
    l4= chr(de4)
    li.append(l1)
    li.append(l2)
    li.append(l3)
    li.append(l4)
    j= str(li)
    w= j.replace("[","")
    w= w.replace("]","")
    w= w.replace(",","")
    w= w.replace("''", "")
    w= w.replace(" ","")
    w= w.replace("'", "")
    return (w)

