def validar_expresion(expresion):
    l = [-1,5]
    if expresion == "2+3" or expresion == "2-3":
      return True
    else:
      return False
       
 

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           