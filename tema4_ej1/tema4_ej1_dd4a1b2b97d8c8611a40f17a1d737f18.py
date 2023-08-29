import random 
def ocultar_letras(palabra,cantidad):
    secreto=[]
    for i in palabra:
        secreto.append(i)
    re="_"
    it=0
    while it<=cantidad:
        se=random.randint(1,len(secreto)-1)
        a=secreto.index(secreto[se])
        secreto[a]=re
        it+=1
    secreto="".join(secreto)
    return secreto

def revisar_letra(palabra_secreta,palabra,letra):
    p=[]
    palabra=list(palabra)
    po=list(letra)
    pu=list(palabra_secreta)
    for letra in palabra:
        if letra=="_":
            p.append(palabra.index(letra))
            i=palabra.index(letra)
            palabra[i]="+"
        else:
            continue
    for letra in palabra:
        for l in po:
            if letra=="+":
                j=palabra.index(letra)
                palabra[j]=l
                if pu[j]==palabra[j]:
                    continue
                else:
                    palabra[j]="_"
                    continue
            else:
                continue
    palabra="".join(palabra)
    return palabra
if __name__ == "__main__":
    r=revisar_letra("lepidoptero","le_i_opter_","pdo")
    print(r)