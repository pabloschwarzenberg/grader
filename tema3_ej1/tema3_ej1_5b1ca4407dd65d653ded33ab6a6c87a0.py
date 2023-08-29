# completa el código de la función
def suma_divisores(a):
    divisores=[1]
    for divisor in range(1,a-1):
        if a%divisor==0:
            divisores.append(divisor)

    resultado=sum(divisores)
    resultado_final=resultado-1
    if resultado_final==1:
        return(resultado_final,True)

    else:
        return(resultado_final,False)
    
    


