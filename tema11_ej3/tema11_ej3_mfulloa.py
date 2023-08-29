#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,lista1,lista2):
    cont=0
    cont2=0
    signo=""
    num=""
    y=len(expresion)-1
    for x in range(len(expresion)):
        if expresion[x]=="+" or expresion[x]=="-":
            cont+=int(num)
            num=""
            break
        elif expresion[x]!="-" and expresion[x]!="+":
            num+=expresion[x]
    for x in range(len(expresion)):
        if expresion[x]!="-" and expresion[x]!="+":
            num+=expresion[x]
            if x==y and signo=="+":
                cont+=int(num)
            elif x==y and signo=="-":
                cont-=int(num)
        elif expresion[x]=="+" and signo=="":
            num=""
            signo="+"
        elif expresion[x]=="-" and signo=="":
            num=""
            signo="-"
        elif expresion[x]=="-" and signo=="-":
            cont-=int(num)
            num=""
            signo="-"
        elif expresion[x]=="-" and signo=="+":
            cont+=int(num)
            num=""
            signo="-"
        elif expresion[x]=="+" and signo=="-":
            cont-=int(num)
            num=""
            signo="+"
        elif expresion[x]=="+" and signo=="+":
            cont+=int(num)
            num=""
            signo="+"
    return(cont)

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           