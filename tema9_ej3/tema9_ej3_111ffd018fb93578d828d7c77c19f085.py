def decodificar(mensaje):
    list= []
    a= mensaje.replace("'", "")
    a= mensaje.replace(",", " ")
    x1= a[0:8] #9 coma
    x2= a[9:17]#18 coma
    x3= a[18:26]#27 coma
    x4= a[27:35]#36 fin
    de1= int(str(x1), int(2))
    de2= int(str(x2), int(2))
    de3= int(str(x3), int(2))
    de4= int(str(x4), int(2))
    l1= chr(de1)
    l2= chr(de2)
    l3= chr(de3)
    l4= chr(de4)
    list.append(l1)
    list.append(l2)
    list.append(l3)
    list.append(l4)
    g= str(list)
    y= g.replace("[","")
    y= y.replace("]","")
    y= y.replace(",","")
    y= y.replace("''", "")
    y= y.replace(" ","")
    y= y.replace("'", "")
    return (y)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         