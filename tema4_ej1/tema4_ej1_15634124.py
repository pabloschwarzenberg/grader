import random
palabras = ["rascacielos", "estatua", "chocolate", "ruinas", "bulldog","lepidoptero"]
palabra= random.choice(palabras)
cantidad = random.randint(1,len(palabra)-1)
def ocultar_letras(palabra,cantidad):
    
    s1=list(palabra)
    palabra_secreta=s1
    i=0
    while i<cantidad:
        m=random.randint(0,len(palabra)-1)
        while palabra_secreta[m]!="_":
            palabra_secreta[m]="_"
            i=i+1
    
    palabra_secreta="".join(palabra_secreta)
    return palabra_secreta

def revisar_letra(palabra,palabra_secreta,letra):
    s1=list(palabra_secreta)
    s2=list(palabra)
    i=0
    while i<len(s1):
        if letra == s2[i]:
            s1[i] = letra
        if letra != s2[i]:
            s1=s1
        i=i+1
    s1="".join(s1)
    return s1
    if palabra == palabraa:
        return palabra
    
if __name__ == "__main__":
    palabraa=input("adivina la palabra: ")
    letra=input("adivina una letra: ")
    palabra_secreta=ocultar_letras(palabra,cantidad)
    revisar_letra(palabra_secreta,palabraa,letra)