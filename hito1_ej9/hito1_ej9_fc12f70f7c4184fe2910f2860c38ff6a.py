#Sistema de Ecuaciones
def sis(ecuacion):
    lista=[]
    for x in ecuacion:
        lista.append(int(x))
    a=lista[0]
    b=lista[1]
    c=lista[2]
    d=lista[3]
    e=lista[4]
    f=lista[5]
    det=a*e-b*d
    listap=["x=","y="]
    if det!=0:
        x=(c*e-b*f)/det
        y=(a*f-c*d)/det
        print("x=",x,"y=",y)
    return ""