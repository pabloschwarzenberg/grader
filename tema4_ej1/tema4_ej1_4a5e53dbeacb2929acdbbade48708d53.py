import random
def ocultar_letras(palabra,cantidad):
    rp=list(palabra)
    for j in range(0,cantidad):        
        g=random.randint(0,len(rp)-1)
        
        while(rp[g]=="_"):
          g=random.randint(0,len(rp)-1)
        f=rp[g]
        rp[g]="_"    
        
    rp="".join(rp)
    return rp

def revisar_letra(palabra_secreta,palabra,letra):
    a=palabra_secreta
    b=palabra
    l=letra
    for i in range(0,len(b)):
        if (b[i]=="_"):            
            if(letra==a[i]):
                b=list(b)
                b[i]=letra
                b="".join(b)
    return b

if __name__ == "__main__":
    pass
         