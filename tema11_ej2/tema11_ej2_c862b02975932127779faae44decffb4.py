def validar_expresion(expresion):
    expre=list(expresion)
    if expre!=[]:
     if expre[0].isdigit()==True or (len(expre)!=1 and expre[0] in "+-" and expre[1].isdigit()==True ):
       expre.pop(0)
       expre="".join(expre)
       return validar_expresion(expre)
     else:
      return False
    else:
      return True
     

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           