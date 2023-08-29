def suma_divisores(numero):
    lista_d=[]
    for divisor in range(1,(numero-1)):
        if numero % divisor == 0 :
            
            lista_d.append(divisor)
    if sum(lista_d)==1:
        return sum(lista_d),True
    else:
        return sum(lista_d),False
        
        
            
           
    