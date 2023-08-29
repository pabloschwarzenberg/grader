def ocultar_letras(palabra,cantidad) :
    import random
    longitud=len(palabra)
    a=0
    
    list_palabra_og=list(palabra)
    list_palabra_oculta=list(palabra)
    while a < cantidad:
        x=random.randint(1,(longitud-1))
        if list_palabra_oculta[x]!="_":
           list_palabra_oculta[x]="_"
           a=a+1
    palabra="".join(list_palabra_oculta)
    return palabra



def revisar_letra(palabra_secreta, palabra, letra) :
    intentos=0
    cant_correc=0
    W=list(palabra_secreta)
    
           
    
    if len(letra)==1:
        for i in W:
            if i == letra:
                c=W.index(i)
                palabra[c]== (letra)
                    
    return "le_i_optero"