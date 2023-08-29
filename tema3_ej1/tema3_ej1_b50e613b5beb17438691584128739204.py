# completa el código de la función
def suma_divisores(numero):
    
    divisor_candidato=0
    suma=0
    while divisor_candidato < numero-1:
        divisor_candidato = divisor_candidato + 1
       
        
        if numero % divisor_candidato == 0:
            suma = suma + divisor_candidato
        
           
            

    if suma==1:
        p=True
    else:
        p=False


    return suma,p

if __name__ == "__main__":

    

    numero=int(input("ingrese numero:"))
    suma,p=suma_divisores(numero)

    print("("+str(suma)+",",str(p)+")")
