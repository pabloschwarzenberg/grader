def suma_divisores(a):
    div=[i for i in range(1,a) if a%i==0]
    resul=sum(div)
    if resul==1:
        return resul,True
    return resul,False
    
 