def validar_expresion(expresion,masmenos=0):
    if len(expresion)==0:
        if masmenos==3: return True
        else: return False
    try:
        int(expresion[0])
        if masmenos==0 or masmenos==1: return validar_expresion(expresion[1:],1)
        elif masmenos==2: return validar_expresion(expresion[1:],3)
    except:
        if masmenos!=1: return False
        if masmenos==1: return validar_expresion(expresion[1:],2)

