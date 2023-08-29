def validar_expresion(expresion):
    lista_expresion=list(expresion)
    numeros="1234567890"
    lista_num=list(numeros)
    contador=[]
    marcador=[]
    for elemento in lista_expresion:
        if elemento is not lista_num:
            return False
        elif elemnto=="-" or elemento=="+":
            contador.append(0)
        elif elemento is lista_num:
            marcador.append(0)
    if len(contador)>1:
        return False
    elif len(contador)==1 and len(marcador)==2:
        return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           