def numero_perfecto(numero):
    
    divisor_candidato=0
    suma=0
    while divisor_candidato < numero-1:
        divisor_candidato = divisor_candidato + 1
       
        
        if numero % divisor_candidato == 0:
            suma = suma + divisor_candidato
        
           
            

    if suma==numero:
        p=True
    else:
        p=False


    return p

if __name__ == "__main__":

    

    numero=int(input("ingrese numero:"))
    p=numero_perfecto(numero)

    print(str(p))