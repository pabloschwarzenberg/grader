def decodificar(mensaje):
    l= []
    x= mensaje.replace("'", "")
    x= mensaje.replace(",", " ")
    x1= x[0:8]
    x2= x[9:17]
    x3= x[18:26]
    x4= x[27:35]
    y1= int(str(x1), int(2))
    y2= int(str(x2), int(2))
    y3= int(str(x3), int(2))
    y4= int(str(x4), int(2))
    l1= chr(y1)
    l2= chr(y2)
    l3= chr(y3)
    l4= chr(y4)
    l.append(l1)
    l.append(l2)
    l.append(l3)
    l.append(l4)
    k= str(l)
    d= k.replace("[","")
    d= d.replace("]","")
    d= d.replace(",","")
    d= d.replace("''", "")
    d= d.replace(" ","")
    d= d.replace("'", "")
    return (d)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         