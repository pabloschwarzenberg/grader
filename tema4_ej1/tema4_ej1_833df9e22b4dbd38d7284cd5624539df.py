def ocultar_palabra(palabra,cantidad):
    lista=list(palabra)
    resultado=[]
    #contador de elementos por ocultar
    i=0
    #contador de elementos que tiene la palabra(posicion de la palabra por ocultar)
    f=0
    #contador de elementos no ocultos(caso especifico)
    t=0
    #primero realizamos el caso de que la palabra sea par
    if(len(palabra)%2)==0:
         while i<int(cantidad):
    #en el caso de que el i no supere la mitad del largo de palabra
            if f<len(palabra):
                resultado.append(lista[f])
                resultado.append("_")
                i+=1
                f+=2
            else:
                resultado[(2*t)]="_"
                t+=1
                i+=1
      while len(resultado)<len(palabra):
                 p=len(resultado)
                 resultado.append(lista[p])
    elif (len(palabra)%2)==1:
        while i<int(cantidad):
            if f<(len(palabra)-1):
                 resultado.append(lista[f])
                 resultado.append("_")
                 i+=1
                 f+=2

            #en el caso de que el i supere la mitad de la palabra
            #seguimos el mismo patron recordando que el ultimo elemento no se encuentra en resultados
            elif i<=f:
                resultado[(2*t)]="_"
                t+=1
                i+=1
        #si el i es menor que la mitad del largo de la palabra
        while len(resultado)<(len(palabra)-1):
               p=len(resultado)
               resultado.append(lista[p])

        #como paso final agregaremos como resultado el ultimo elemento de la lista
        if i<len(palabra):
            resultado.append(lista[-1])

        #en el caso que el i sea igual a la cantidad de palabra todo se oculta
        elif i==len(palabra):
            texto=(len(palabra)*"_")
            resultado=list(texto)



    #como ultimo paso pasamos toda la lista de resultado a un string
    string=""
    for elemento in resultado:
        string+=str(elemento)

    return string
    
def revision_letra(palabra_secreta,palabra,letra):
    i=0
    posicion=[]
    while i<len(palabra):
        if palabra[i]is "_":
            posicion.append(i)
        i+=1

    desifrar=[]
    for elemento in posicion:
        desifrar.append(palabra_secreta[elemento])

    comparado=[]
    resultado=""

    if len(letra)==1:
        for incognita in desifrar:
            if incognita is letra:
                comparado.append(letra)
            else:
                comparado.append("_")

        k=0
        j=0

        while k<len(palabra):
            if k == posicion[j]:
                resultado+=str(comparado[j])
                if j<len(posicion)-1:
                    j+=1
                k+=1
            else:
                resultado+=str(palabra[k])
                k+=1

    elif len(letra)>1:
        if letra is palabra_secreta:
            resultado+=str(palabra_secreta)

        else:
            resultado+=str(palabra)
    return resultado

