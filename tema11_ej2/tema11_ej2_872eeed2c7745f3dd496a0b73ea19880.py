def validar_expresion(expresion):

    lista=expresion.split()

    largo=len(expresion)

    if largo==1:

        if expresion[0].isdigit()==True:
            return True
        else:
            return False

    elif largo==3:

        if expresion[0].isdigit()==True and expresion[1].isdigit()==False and expresion[2].isdigit()==True:
            return True
        else:
            return False

    expresion2=expresion[2:largo-2]

    if expresion[0].isdigit()==True and expresion[1].isdigit()==False and expresion[largo-1].isdigit()==True and expresion(largo-2).isdigit()==False:

        if validar_expresion(expresion2):

            return True
        else:
            return False

    else:
        return False
    
        
        



    
    return

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           