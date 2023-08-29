def levenshtein(palabra1,palabra2):
    p1=[]
    p2=[]
    distancia=0
    comparacion=[]
    for x in palabra1:
        p1.append(x)
    for i in palabra2:
        p2.append(i)
    for i in p1:
        if i in p2:
            comparacion.append(i)
    if len(palabra1) > len(palabra2):
        distancia=(len(palabra1)-len(comparacion))
    if len(palabra1) < len(palabra2):
            distancia = (len(palabra2) - len(comparacion))
    if len(palabra1)==len(palabra2):
        distancia = (len(palabra2) - len(comparacion))

    if distancia > 1 :
        return("+1")
    if distancia == 1  and (len(p1)-len(p2)!=0 or len(p2)-len(p1)!=0 ):
        return("IB")
    if distancia ==1 and len(p1)-len(p2)==0 :
        return("1S")
    if distancia==0:
      return ("0D")
