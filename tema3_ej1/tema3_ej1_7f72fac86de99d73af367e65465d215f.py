# completa el código de la función
def suma_divisores(a):
    factores=[]
    respuesta=[]
    divisor=2
    divisores=0
    while divisor<=a/2:
        if a%divisor==0:
            factores.append(divisor)
        if divisor**2==a:
            factores.append(divisor)
        divisor+=1
    i=0
    while i<len(factores):
        divisores=divisores+factores[i]
        i+=1
    if a!=1:
        divisores+=1
    respuesta.append(divisores)
    if a==1:
        respuesta.append(False)
    else:
        if divisores==1:
            respuesta.append(True)
        else:
            respuesta.append(False)
    respuesta=tuple(respuesta)
    return respuesta