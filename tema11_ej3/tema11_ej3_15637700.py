#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha

def evaluar_expresion(expresion,operandores,operandos):
    num = "1234567890"
    op = "+-"
    suma = 0
        
    if len(expresion)<1:
        return 0

    
    elif expresion[0] in op and expresion[1] in num:
        if len(expresion)>=3:
            if expresion[2] in num:
                if expresion[0]==op[0]:
                    suma += int(expresion[1:3])
                    n = suma
                    return n + evaluar_expresion(expresion[3:],operandores,operandos)
                else:
                    suma -= int(expresion[1:3])
                    n = suma
                    return n + evaluar_expresion(expresion[3:],operandores,operandos)
        else:
            if expresion[0]==op[0]:
                suma += int(expresion[1])
                n = suma
                return n + evaluar_expresion(expresion[2:],operandores,operandos)
            else:
                suma -= int(expresion[1])
                n = suma
                return n + evaluar_expresion(expresion[2:],operandores,operandos)
                

    elif expresion[1] in op and expresion[2] in num:
        if len(expresion)>4:
            if expresion[3] in num:
                if expresion[1]==op[0]:
                    suma += int(expresion[0]) + int(expresion[2:4])
                    n = suma
                    return n + evaluar_expresion(expresion[4:],operandores,operandos)
                else:
                    suma += int(expresion[0]) - int(expresion[2:4])
                    n = suma
                    return n + evaluar_expresion(expresion[4:],operandores,operandos)
            else:
                if expresion[1]==op[0]:
                    suma += int(expresion[0]) + int(expresion[2])
                    n = suma
                    return n + evaluar_expresion(expresion[3:],operandores,operandos)
                else:
                    suma += int(expresion[0]) - int(expresion[2])
                    n = suma
                    return n + evaluar_expresion(expresion[3:],operandores,operandos)

        elif len(expresion)==4:
            if expresion[3] in num:
                if expresion[1]==op[0]:
                    suma += int(expresion[0]) + int(expresion[2:])
                    n = suma
                    return n 
                else:
                    suma += int(expresion[0]) - int(expresion[2:])
                    n = suma
                    return n 
        elif len(expresion)==3:
            if expresion[1]==op[0]:
                suma += int(expresion[0]) + int(expresion[2])
                n = suma                        
                return n 
            else:
                suma += int(expresion[0]) - int(expresion[2])
                n = suma
                return n 
        


if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           