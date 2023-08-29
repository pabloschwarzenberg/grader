import random
L=["lepidoptero"]

def ocultar_letras(palabra,cantidad):
    palabra=L
    n=cantidad
    a=palabra[random.randint(0,0)]
    palabra=list(a)
    while n>0:
        b=random.randint(0,len(a)-1)
        if palabra[b]!="_":
            palabra[b]="_"
            n-=1
        else:
            pass
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
        return palabra

if __name__ == "__main__":
    pass
         