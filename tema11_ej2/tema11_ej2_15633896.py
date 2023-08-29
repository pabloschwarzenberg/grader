def validar_expresion(expresion):
    def funcion(expresion,lista=[]):
        numeros="0123456789"
        if len(expresion)==0:
            numero=lista.count("s")
            if numero==0:
                return False
            else:
                suma=0
                lista1="".join(lista)
                posicion=lista1.find("s")
                if lista[(int(posicion)-1)]=="n" and lista[(int(posicion)+1)]=="n":
                    return True
                        
                else:
                     return False
                

        a=expresion[0]

        if numeros.find(a)==-1:
            nuevalista=lista+["s"]
        else:
            nuevalista=lista+["n"]
        return funcion(expresion[1:],nuevalista)
    return(funcion(expresion))
           