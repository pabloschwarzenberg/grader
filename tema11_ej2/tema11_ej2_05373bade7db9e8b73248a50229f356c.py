def validar_expresion(expresion):
    if len(expresion)==1:
        if expresion.isnumeric()==True:
            return True
        else:
            return False
    else:
       if len(expresion)%2==0:
           if expresion[0].isnumeric()==False:
               return validar_expresion(expresion[1:])
           else:
               return False
       else:
           if expresion[0].isnumeric()==True:
               return validar_expresion(expresion[1:])
           else:
               return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           