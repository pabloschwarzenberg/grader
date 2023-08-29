def validar_expresion(expresion):
    lista=list(expresion)
    print(len(expresion))
    print(lista)
    lista_signos=['+','-']
    for i in range(len(lista)):
        if lista[len(expresion)-1] in lista_signos:
            return False
        
        elif lista[i] in lista_signos and lista[i+1] in lista_signos:
            return False
        else:
        
            return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           