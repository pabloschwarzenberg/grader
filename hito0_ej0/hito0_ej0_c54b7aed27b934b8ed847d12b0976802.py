def interpretar(expresion):
    ex = list(expresion.strip())
    ex.append("")
    expres = []
    s = ""
    for crt in ex:
        if crt.isnumeric():
            s = s + crt
        elif crt != ex[-1]:
            expres.append(float(s))
            expres.append(crt)
            s = ""
        else:
            expres.append(float(s))
    operaciones=["/","*","-","+"]
    for operacion in operaciones:
        result = []
        cont=0
        while cont<len(expres):
            if expres[cont]==operacion:
                res=0
                if operacion=="/":res=result[-1]/expres[cont+1]
                elif operacion=="*":res = result[-1] * expres[cont + 1]
                elif operacion == "-":res=result[-1]-expres[cont+1]
                elif operacion=="+":res=result[-1]+expres[cont+1]
                del result[-1]
                result.append(res)
                cont=cont+1
            else:
                result.append(expres[cont])
            cont=cont+1
        expres=result.copy()
        
    return expres[0]

resultado = interpretar("2*3+5+6*7/9")
print(resultado)
# el resultado debiera ser 15.66666
      