def interpretar(expresion):
    try:
        expresion = list(expresion)
        i=0
        while i<len(expresion):
            if expresion[i].isdigit():
                if expresion[i+1].isdigit():
                    expresion[i:i+2] = [expresion[i]+expresion[i+1]]
            i += 1
    except:
        expresion = expresion
    try:
        if len(expresion)==1:
            return expresion[0]
        if '*' in expresion:
            pm = expresion.index('*')
            rm = float(expresion[pm-1])*float(expresion[pm+1])
            expresion[pm-1:pm+2] = [rm]
            return interpretar(expresion)
        elif '/' in expresion:
            pd = expresion.index('/')
            rd = float(expresion[pd-1])/float(expresion[pd+1])
            expresion[pd-1:pd+2] = [rd]
            return interpretar(expresion)
        elif '+' in expresion:
            ps = expresion.index('+')
            rs = float(expresion[ps-1])+float(expresion[ps+1])
            expresion[ps-1:ps+2] = [rs]
            return interpretar(expresion)
        elif '-' in expresion:
            pr = expresion.index('-')
            rr = float(expresion[pr-1])-float(expresion[pr+1])
            expresion[pr-1:pr+2] = [rr]
            return interpretar(expresion)
    except:
        return 'Expresión inválida.'

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666