def buscarTodas(a,b):
    cadena=a
    x=0
    el_numero=[]
    espacio=" "
    while x < len(cadena):
        f=cadena[x]
        if f==b:
            el_numero.append(str(x))
        x+=1
        elnumerodenumeros=espacio.join(el_numero)
    return(elnumerodenumeros)

           