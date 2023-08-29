import random

def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    for i in range(cantidad):
        j=random.randint(0,len(palabra)-1)
        if palabra[j]=="_":
            j=random.randint(0,len(palabra)-1)
        palabra.pop(j)
        palabra.insert(j,"_")
    palabra=''.join(palabra)    
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    palabra_secreta=list(palabra_secreta)
    for i in range(len(palabra)):
        if palabra[i]=="_":
            if palabra_secreta[i]==letra:
                palabra.pop(i)
                palabra.insert(i,letra)
    palabra=''.join(palabra) 
    return palabra

if __name__ == "__main__":
    pass

    palabras=["knäckebröd", "mat", "läsk", "tårta", "fanta", "kanelbulle"]
    p_s=random.choice(palabras)
    c=random.randint(0,len(p_s)-1)
    p=ocultar_letras(p_s,c)

    i=0
    while p!=p_s and i!=7:
        print(p)
        o=input("Advinar la palabra: ")
        if len(o)==1:      
            p=revisar_letra(p_s,p,o)
            if p==p_s:
                print("La palabra secreta es: " + p)
                print("Correcto!")
                break
        elif o==p_s:
            p=o
            print("Correcto!")
            print("La palabra secreta es: " + p)
            break
        else:
            i+=1
    if p!=p_s:
        print("Perdiste!")
    if p==p_s and i==7:
        print("Correcto!")