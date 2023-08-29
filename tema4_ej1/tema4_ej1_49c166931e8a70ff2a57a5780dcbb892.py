import random
def buscartodas(a,b):
    i=0
    l=[]
    while i<len(a):
        if a[(i)]==b:
            l.append(i)
        i=i+1
    return l
def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    c=0
    while c<cantidad:
        r=random.randint(0,len(palabra)-1)
        while palabra[r]=="_":
            r=random.randint(0,len(palabra)-1)
        palabra[r]="_"
        c=c+1
    palabra="".join(palabra)    
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    p=buscartodas(palabra_secreta,letra)
    palabra=list(palabra)
    for i in p:
        palabra[i]=letra
    palabra="".join(palabra)   
    return palabra

if __name__ == "__main__":
    lpal=["calidez","empatia","retroalimentacion","hipoteticamente","alcornoque"]
    p=random.choice(lpal)
    po=ocultar_letras(p,(len(p)-3))
    ci=0
    print(po)
    while ci<7 and not(p==po):
        j=input(" ingresar una letra(1), ingresar la palabra(2)")
        while not(j=="2" or j=="1"):
            print("no ingreso ni 1 ni 2")
            j=input(" ingresar una letra(1), ingresar la palabra(2)")
        if j=="1":
            i=input("ingrese la letra")
            if revisar_letra(p,po,i)==po:
                ci=ci+1
            else:
                po=revisar_letra(p,po,i)
            print(po)
            print("le quedan",7-ci,"intentos")
        if j=="2":
            i=input("ingrese la palabra")
            if i==p:
                po=p
            else:
                ci=7
    if ci==7:
        print("no has adivinado la palabra , intentalo nuevamente")
    if p==po:
        print("felicitaciones has adivinado la palabra")
         