def rot13(palabra):
    abc =["a" ,"b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l" ,"m" ]
    nop =["n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z" ]
    pal_dec = []
    for letra in palabra:
        if letra in abc:
            pos = abc.index(letra)
            letra = nop[pos]
            pal_dec.append(letra)
        elif letra in nop:
            pos_2 = nop.index(letra)
            letra = abc[pos_2]
            pal_dec.append(letra)
            
    codificado = "".join(pal_dec)
    return codificado
           