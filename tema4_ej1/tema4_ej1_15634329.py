import random
L=["lepidoptero","hidroplano","cohete","caviar","rucula","galicia","andaluz","minucioso"]
palabra=L[random.randint(0,7)]
cantidad=random.randint(1,len(palabra)-2)

def ocultar_letras(palabra,cantidad):
    L=[];p=len(palabra)
    for i in range(p):
        L.append(palabra[i])
    while cantidad>0:
        e=random.randint(0,p-1)
        if L[e]!="_":
            L[e]="_"
            cantidad-=1
    palabra=""
    for i in range(p):
        palabra=palabra+L[i]
    return palabra
    
def revisar_letra(palabra_secreta,palabra,letra):
    L=[]
    for i in range(len(palabra_secreta)):
        if palabra[i]=="_" and palabra_secreta[i]==letra:
            L.append(letra)
        else:
            L.append(palabra[i])
    palabra=""
    for i in range(len(palabra_secreta)):
        palabra=palabra+L[i]
    return palabra




if __name__ == "__main__":
    p=ocultar_letras(palabra,cantidad)
    print ("Tienes 7 intentos para adivinar la siguiente palabra:",p)
    x=0
    while p!=palabra and x<7:
        x+=1
        s=input("Adivina la palabra o una de sus letras: ")
        if len(s)!=1:
            if s==palabra:
                p=s
            else :
                print("No adivinaste")
        else:
            p=revisar_letra(palabra,p,s)
            print("Letras conocidas: ",p)
    if p==palabra:
        print("Adivinaste")
    else:
        print("No adivinaste. La palabra es",palabra)         