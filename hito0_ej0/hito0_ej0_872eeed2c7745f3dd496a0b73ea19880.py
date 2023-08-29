def interpretar(expresion):

    if len(expresion)==3:
        a=float(expresion[0])
        b=float(expresion[2])
        signo=expresion[1]

        if signo=="/":
            return a/b
        elif signo=="*":
            return a*b
        elif signo=="+":
            return a+b
        elif signo=="-":
            return a-b
        
        

    division=expresion.find("/")
    multiplicacion=expresion.find("*")
    resta=expresion.find("-")
    suma=expresion.find("+")

    if division>0:

        lista=list(expresion)

        sublista=lista[division-1:division+2]

        numero=float(sublista[0])/float(sublista[2])

        lista[division-1:division+2]=str(numero)

        string="".join(lista)

        interpretar(string)

    elif multiplicacion>0:

        lista=list(expresion)

        sublista=lista[multiplicacion-1:multiplicacion+2]

        a=float(sublista[0])
        b=float(sublista[2])

        numero=a*b

        lista[multiplicacion-1:multiplicacion+2]=str(numero)

        string="".join(lista)

        interpretar(string)

    elif resta>0:

        lista=list(expresion)

        sublista=lista[resta-1:resta+2]

        numero=float(sublista[0])-float(sublista[2])

        lista[resta-1:resta+2]=str(numero)

        string="".join(lista)

        interpretar(string)

    elif suma>0:

        lista=list(expresion)

        sublista=lista[suma-1:suma+2]

        numero=float(sublista[0])+float(sublista[2])

        lista[resta-1:resta+2]=str(numero)

        string="".join(lista)

        interpretar(string)
        
        pass


resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
      