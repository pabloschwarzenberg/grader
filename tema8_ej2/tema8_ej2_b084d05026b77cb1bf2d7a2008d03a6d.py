def buscarTodas(a,b):
    a= list(a)
    l=[]
    largo_a= len(a)
    largo_b= len(b)
    if len(b)==1:
        for i in range(0, largo_a):
            if a[i]== b:
                l.append(str(i)+ " ")    
        l= "".join(l)
        respuesta = l
    elif largo_b > 1 and largo_b <= largo_a:
        a= "".join(a)
        posicion=0
        k=0
        while len(a)>0 and posicion != -1:
            posicion = a.find(b)
            if posicion == -1:
                break
            l.append(str(posicion + k)+ " ")
            a= a[posicion + largo_b:]
            k = k + posicion + largo_b
        l = "".join(l)
        respuesta = l
    if len(l)==0:
        respuesta= False
    else:
        respuesta = respuesta.strip(respuesta[-1])
    return respuesta
if __name__ == "__main__":
    pass
           