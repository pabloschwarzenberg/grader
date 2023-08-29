def validar_expresion(expresion,i=0):
    exp = list(expresion)
    if i in [0,len(exp)-1] and exp[i] in ["-","+"]:
        return False
    elif i == len(exp)-1:
        return True
    else:
        i+=1
        return validar_expresion(exp,i)
           