def evaluar_expresion(expresion,operandores,operandos):
    ex=list(str(expresion))
    exn=expresion
    ls=operandores
    ln=operandos
    if operandores!=[]:
        if exn=='0':
          exn=ln.pop(0)
        exn=(str(exn))+str(ls.pop(0))+str(ln.pop(0))
        exn=eval(exn)
        #exn=str(exn)
        return evaluar_expresion(exn,ls,ln)
    elif ln==ls==[] and (len(ex))<3:
        r=exn
        return r
    else:
        n=''
        for letra in ex:
            if letra=='+' or letra=='-':
                p=ex.index(letra)
                for i in range(0,p):
                    n+=str(ex.pop(i))
                ln.append(n)
                ls.append(ex.pop(0))
        lex=len(ex)
        n=''
        for i in range(0,lex):
            n=n+str(ex[i])
        ln.append(n)
        return evaluar_expresion('0',ls,ln)

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           