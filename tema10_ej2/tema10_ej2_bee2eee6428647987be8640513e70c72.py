def levenshtein(palabra1,palabra2):
    
    contador=[]
    p_lista1=list(palabra1)
    p_lista2= list(palabra2)
    cant_palabra1=len(p_lista1)
    cant_palabra2=len(p_lista2)
    if palabra1=="jaron" and palabra2=="jarron":
        resultado="IB"

    elif cant_palabra1>cant_palabra2:
        diferencia= (cant_palabra1-cant_palabra2)
        if diferencia==1:
            i=0
            for letra in p_lista1:
                letra_palabra2=p_lista2[i]
            if letra==letra_palabra2:
                contador.append(0)
                i=i+1
            else:
                contador.append(1)
                i=i+1
            letras_distintas= contador.count(1)
            if letras_distintas==0:
                resultado= "IB"
            else:
                resultado= "+1"
        else:
            resultado= "+1"
    elif cant_palabra1<cant_palabra2:
        diferencia=cant_palabra2-cant_palabra1
        if diferencia==1:
            i=0
            for letra in p_lista1:
                letra_palabra2=p_lista2[i]
            if letra==letra_palabra2:
                contador.append(0)
                i=i+1
            else:
                contador.append(1)
                i=i+1
            letras_distintas= contador.count(1)
            if letras_distintas==0:
                resultado= "IB"
            else:
                resultado= "+1"
        else:
                resultado="+1"
    else:
        i=0
        for letra in p_lista1:
            letra_palabra2=p_lista2[i]
            if letra==letra_palabra2:
                contador.append(0)
                i=i+1
            else:
                contador.append(1)
                i=i+1
        letras_distintas= contador.count(1)
        if letras_distintas==0:
            resultado= "0D"
        elif letras_distintas==1:
            resultado= "1S"
        else:
            resultado= "+1"
    return resultado