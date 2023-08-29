def validar_expresion(expresion, i = 0):
    signos = ["+" , "-"]
    if len(expresion) == 0:
        return True
    if i == 0:
        if expresion[0].isdigit() and expresion[len(expresion)-1].isdigit():
            i +=1
            return validar_expresion(expresion[1:-1],i)
        else:
            return False
    
    if not expresion[0].isdigit() and not expresion[0] in signos:
        return False
    return validar_expresion(expresion[1:],i)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           