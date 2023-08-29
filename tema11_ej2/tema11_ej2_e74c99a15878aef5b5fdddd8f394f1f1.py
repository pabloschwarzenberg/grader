def validar_expresion(expresion):
    if expresion.isdigit():
        return True
    elif len(expresion)==1:
        return False
    try:
        if expresion[0].isdigit() and not expresion[1].isdigit() and not expresion[1].isalpha():
            return validar_expresion(expresion[2:len(expresion)+1])
    except:
        pass
    return False