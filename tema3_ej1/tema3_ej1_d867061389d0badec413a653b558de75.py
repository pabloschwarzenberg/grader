# completa el código de la función
def suma_divisores(a):
    div=1
    contador=0
    for div in range(1,a):
        if a%div==0:
            contador+=div
            div+=1
        else:
            div+=1
    if contador==1:
        return contador, True
    else: 
        return contador, False 
    
if __name__=="__main__":
    pass