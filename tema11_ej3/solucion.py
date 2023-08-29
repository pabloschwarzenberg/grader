def evaluar_expresion(s,operadores,operandos):
    suma=s.find("+")
    resta=s.find("-")
    if suma==-1 and resta==-1:
        if s.isdigit():
            operandos.append(int(s))
            r=0
            for operador in operadores:
                a=operandos[0]
                b=operandos[1]
                operandos=operandos[2:]
                if operador=="+":
                    operandos.insert(0,a+b)
                else:
                    operandos.insert(0,a-b)
            return operandos.pop()
    elif suma!=-1 and resta!=-1:
        if suma<resta:
            a=s[:suma]
            b=s[suma+1:]
            operandos.append(int(a))
            operadores.append("+")
            return evaluar_expresion(b,operadores,operandos)
        else:
            a=s[:resta]
            b=s[resta+1:]
            operandos.append(int(a))
            operadores.append("-")
            return evaluar_expresion(b,operadores,operandos)
    elif suma!=-1:
        a=s[:suma]
        b=s[suma+1:]
        operandos.append(int(a))
        operadores.append("+")
        return evaluar_expresion(b,operadores,operandos)
    elif resta!=-1:
        a=s[:resta]
        b=s[resta+1:]
        operandos.append(int(a))
        operadores.append("-")
        return evaluar_expresion(b,operadores,operandos)

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
