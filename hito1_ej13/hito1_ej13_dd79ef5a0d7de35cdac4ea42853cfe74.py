def obtener_numero_primo(numero_maximo):
    numeros=[True,True]+[True]*(numero_maximo-1)
    primer_numero_primo=2
    while primer_numero_primo**2<=numero_maximo:
        i+=primer_numero_primo
        while i<=numero_maximo:
            numeros[i]=False
            i+=primer_numero_primo
        j=primer_numero_primo+1
        while j<obtener_numero_primo:
            if numeros[j]:
                primer_numero_primo=j
                break
            j+=1
        i=primer_numero_primo

    return [i+2 for i, not_crossed in enumerate(numeros[2:]) if not_crossed]