def validar_expresion(expresion,contador=0):
    if expresion[0].isdigit()==True:
        contador+=1
        return validar_expresion(expresion[1:],contador)
    elif expresion[0].isdigit()==False and contador==0:
        return False
    else:
        try:
            a=expresion[1]
        except IndexError:
            return False
        else:
            if a.isdigit()==True:
                return True
            else:
                return False  
      
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           