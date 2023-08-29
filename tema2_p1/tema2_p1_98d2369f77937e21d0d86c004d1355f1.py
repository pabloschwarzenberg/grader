# por favor escribe aquí tu función
def es_primo(numero):
    if(numero >1):
        n=0
        b=2
        c= numero%b
        if(c==0):
            n+=1
            b+=1
        if(n==0):
            return True
        else:
            return False
    else:
        return False
try:
    inr = int(input("ingrese numero: "))
    print(es_primo(inr))
except:
    print("Ingrese solo numero porfavor")
    
           