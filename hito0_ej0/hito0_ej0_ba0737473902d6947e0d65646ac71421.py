#Hola profesor;
#No tengo grupo ya que no asisti a la clase del ejercicio.
#Si mi codigo parece mas largo de lo necesario es porque esta optimizado para todo tipo de numeros, por sobre una cifra o con decimales.

def es_numero(x):
    num=[0,1,2,3,4,5,6,7,8,9,0]
    for n in num:
        if str(n)==x[0]:
            return True
    return False

def organizar(ex):
    for i in range(0,len(ex)):
        if es_numero(ex[i])== True or ex[i]==".":
            if i!=0:
                if (es_numero(ex[i-1])== True or ex[i-1]==".") :
                    res=str(ex[i-1]) + str(ex[i])
                    ex.remove(ex[i])
                    ex[i-1]= res
                    return organizar(ex)
    return (ex)

def interpretar(expresion):
    #organicemos la lista
    ex=list(expresion)
    ex=organizar(ex)

    #multiplicaciones y divisiones
    for i in range(len(ex)):
        if ex[i]=="*":
            res= float(ex[i-1])*float(ex[i+1])
            ex.remove(ex[i-1])
            ex.remove(ex[i-1])
            ex[i-1]= str(res)
            return interpretar("".join(ex))
        elif ex[i]=="/":
            res= float(ex[i-1])/float(ex[i+1])
            ex.remove(ex[i-1])
            ex.remove(ex[i-1])
            ex[i-1]= str(res)
            return interpretar("".join(ex))

    #sumas y restas
    for i in range(len(ex)):
        if ex[i] == "+":
            res = float(ex[i - 1]) + float(ex[i + 1])
            ex.remove(ex[i - 1])
            ex.remove(ex[i - 1])
            ex[i - 1] = str(res)
            return interpretar("".join(ex))

        elif ex[i] == "-":
            res = float(ex[i - 1]) - float(ex[i + 1])
            ex.remove(ex[i - 1])
            ex.remove(ex[i - 1])
            ex[i - 1] = str(res)
            return interpretar("".join(ex))


    return ex

resultado = interpretar("2*3+5+6*7/9")
print(resultado)
# el resultado debiera ser 15.66666
