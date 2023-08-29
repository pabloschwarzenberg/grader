def buscarTodas(a,b):
    a.strip("")
    lista=list(a)
    repeticiones=lista.count(b)
    string=""
    for i in range(repeticiones):
        if i>0:
            string+=" "
        posicion=lista.index(b)
        string+=str(posicion)
        lista[posicion]="1"
    string.rstrip( )
    return string