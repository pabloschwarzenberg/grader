#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,operandores,operandos):
    if str(expresion).isnumeric() or (str(expresion)[0]=="-" and str(str(expresion)[1:]).isnumeric()):
        return int(expresion)
    if expresion[0].isnumeric():
        for i in range(0,len(expresion)):
            if expresion[i] in ("+","-"):
                if i-1 != 0:
                    a=int(expresion[0:i-1])
                else:
                    a=int(expresion[0])
                for e in range(i+1,len(expresion)):
                    if expresion[e] in ("+","-"):
                        if i+1 != e-1:
                            b= int(expresion[i+1:e-1])
                        else:
                            b=int(expresion[i+1])
                        if expresion[i]=="+":
                            return evaluar_expresion(str(a+b)+expresion[e:],None,None)
                        if expresion[i]=="-":
                            return evaluar_expresion(str(a-b)+expresion[e:],None,None)
                b=int(expresion[i+1:])
                if expresion[i]=="+":
                        return evaluar_expresion(str(a+b),None,None)
                if expresion[i]=="-":
                        return evaluar_expresion(str(a-b),None,None)
    if not expresion[0].isnumeric():
        for i in range(1,len(expresion)):
            if expresion[i] in ("+","-"):
                a=int(expresion[0:i])
                for e in range(i+1,len(expresion)):
                    if expresion[e] in ("+","-"):
                        if i+1 != e-1:
                            b= int(expresion[i+1:e-1])
                        else:
                            b=int(expresion[i+1])
                        if expresion[i]=="+":
                            return evaluar_expresion(str(a+b)+expresion[e:],None,None)
                        if expresion[i]=="-":
                            return evaluar_expresion(str(a-b)+expresion[e:],None,None)
                b=int(expresion[i+1:])
                if expresion[i]=="+":
                        return evaluar_expresion(str(a+b),None,None)
                if expresion[i]=="-":
                        return evaluar_expresion(str(a-b),None,None)
    return 0

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           