def ocultar_letras(palabra,cantidad):
    import random
    while cantidad != 0:
        a=''
        b=0
        c=len(palabra)
        x=random.randrange(len(palabra))
        if palabra[x] != '_':
            while c!=0:
                if b==x:
                    a+='_'
                    b+=1
                else:
                    a+=palabra[b]
                    b+=1
                c-=1
            palabra=a
            cantidad-=1
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    d=0
    c=0
    b=len(palabra)
    a=''
    for i in palabra_secreta:
        if i==letra:
            while b!=0:
                if palabra[c]=='_' and palabra_secreta[c]==letra:
                    a+=palabra_secreta[c]
                    c+=1
                else:
                    a+=palabra[c]
                    c+=1
                b-=1
            palabra=a
        d+=1
        c=0
        b=len(palabra)
        a=''
    return palabra