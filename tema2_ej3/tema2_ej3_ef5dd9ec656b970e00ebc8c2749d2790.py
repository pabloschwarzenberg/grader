def numero_perfecto(numero1,np=False) :
    numero2=1
    suma=0
    while numero2 < numero1 :
        resto = numero1 % numero2
        
        if resto == 0 :
            suma+= numero2
            
            
        else:
            numero2+1
        numero2+=1    

    if suma == numero1 :
        np = True 
    return  np

           