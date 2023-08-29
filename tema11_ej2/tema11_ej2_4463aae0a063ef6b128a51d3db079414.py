def validar_expresion(expresion):
    if isinstance(expresion,str):
        if expresion[0] in ['+','-']:
            expresion=expresion[1:len(expresion)]
        expresion=expresion.split('+')
        for i in range(len(expresion)):
            extract=expresion.pop(i)
            extract=extract.split('-')
            expresion.extend(extract)
    expresion=list(expresion)
    print(expresion)
    if len(expresion)==0:
        return True
    else:
        if expresion[0]=='':
            return False
        else:
            expresion=expresion[1:len(expresion)]
            return validar_expresion(expresion)


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))