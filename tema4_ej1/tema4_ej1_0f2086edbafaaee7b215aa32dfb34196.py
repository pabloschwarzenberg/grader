def ocultar_letras(palabra,cantidad):
    a=list(palabra)
    for i in range(cantidad):
        import random
        x=random.randint(0,len(palabra)-1)
        while a[x]=="_":
          x=random.randint(0,len(palabra)-1)
        a[x]="_"
        word="".join(a)
    return word

def revisar_letra(palabra_secreta,palabra,letra):
    a=list(palabra_secreta)
    b=list(palabra)
    for i in range(len(a)):
        if letra==a[i]:
            b[i]=letra
    palabra="".join(b)
    return palabra

if __name__ == "__main__":
    lista=["estierco","melayada","elefante"]
    intentos=7
    import random
    palabra_secreta=lista[random.randint(0,4)]
    palabra=ocultar_letras(palabra_secreta,random.randint(0,len(palabra_secreta)-1))
    print(palabra)
    while intentos>0:
       letra=input("ingrese letra:")
       palabra=revisar_letra(palabra_secreta,palabra,letra)
       if palabra==palabra_secreta:
          print(palabra)
          break
       else:
          print(palabra)
       intentos=intentos-1
    if palabra!=palabra_secreta:
         print("no tienes mas intentos")
          
         