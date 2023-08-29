def validar_expresion(expresion):

    # lista de caracteres
    lista_de_caracteres = ['+','-']
    lista_de_numeros = ['0', '1','2','3','4','5','6','7','8','9']
    
    # convertir la expresion en una lista
    expresion = list(expresion)
    
    # revisar que solo haya un caracter + o -
    if expresion.count("-")+expresion.count("+") > 1:
        return False
    
    # revisar por el primer input de la expresion
    caracter = expresion[0]
    
    # revisar que siempre haya un numero despues de un caracter
    if caracter in lista_de_caracteres:
        if len(expresion)<2:
            return False
        elif expresion[1] not in lista_de_numeros:
            return False
        
    # revisar que el caracter sea un numero natural o un "-" o "+" 
    if caracter not in lista_de_caracteres and caracter not in lista_de_numeros:
        return False
    
    # cortar la expresion (i.e. sacar el primer elemento)
    expresion = expresion[1:]
    
    if len(expresion)==0:
        return True
    else:
        "".join(expresion)
        ####### RECURSION #################
        return validar_expresion(expresion)
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           