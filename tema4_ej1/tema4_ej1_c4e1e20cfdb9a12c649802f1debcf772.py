import random
palabra="lepidoptero"

def ocultar_letras(palabra,cantidad):
    i=0
    m=[]
    psecreta=list(palabra)
    p=len(psecreta)-1
    while i<cantidad:
        pos=random.randint(0,p)
        if pos not in m:
            m.append(pos)
            psecreta[pos]="_"
            i+=1
        else:
            i=i
    psecretaa="".join(psecreta)
    return psecretaa

def revisar_letra(palabra,psecreta,letra):
    palabra=list(palabra)
    psecreta=list(psecreta)
    i=0
    while i<len(palabra):
        if palabra[i]==letra:
            psecreta[i]=letra
        i+=1
    palabraf="".join(psecreta)
    return palabraf