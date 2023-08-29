# por favor escribe aquí tu función
def es_primo(numero):
    if numero>1:
        i = 2
        c = 0

#Bucle y condicionantes
        while numero>i and c==0:
            x=numero%i

            if x==0:
                c+=1
            i+=1

        if c==0:
            return True
    
        else:
            return False            
    else:
        return False
#try for another way :(
try:
    n = int(input("Ingrese un numero: "))
    
except:
    pass