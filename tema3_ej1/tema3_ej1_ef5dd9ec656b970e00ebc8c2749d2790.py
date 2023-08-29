def suma_divisores(numero1,primo=False ) :
    numero2=1
    suma=0
    while numero2 < numero1 :
        resto = numero1 % numero2
        
        if resto == 0 :
            suma+= numero2
            
            
        else:
            numero2+1
        numero2+=1    

    if suma == 1 :
        primo = True 
    return  (suma,primo)
        

           