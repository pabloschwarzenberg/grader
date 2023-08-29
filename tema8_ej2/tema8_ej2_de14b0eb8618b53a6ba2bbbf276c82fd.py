def buscarTodas(a,b):
    final=[]
    posicion=0
    for i in a:
        if i == b:
            final.append(str(posicion)+" ")
        posicion=posicion+1
    final="".join(final)
    final2=final[ :-1]
    return final2        