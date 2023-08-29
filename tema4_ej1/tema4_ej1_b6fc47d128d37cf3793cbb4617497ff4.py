def ocultar_letras(palabra,cantidad):
    for i in range(cantidad):
        import random
        x=random.randint(0,len(palabra)-1)
        a=palabra[x]
        if a !="_":
            palabra=palabra[0:x]+palabra[x].replace(a,"_")+palabra[x+1:]
        else:
            cantidad+=1

    return palabra

def revisar_letra(palabra,palabra_secreta,letra):
    lista=[]
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i]=="_":
            lista.append(i)
            if palabra[i]==letra:
                palabra_secreta=palabra_secreta[0:i]+letra+palabra_secreta[i+1:]
    return palabra_secreta
         