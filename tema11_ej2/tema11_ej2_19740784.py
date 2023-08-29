def validar_expresion(expresion):
    exp=list(expresion)
    for i in range(len(exp)-1):
      if str(exp[i]).isalnum() == False and str(exp[i+1]).isalnum() == False :
        return False
    if str(exp[len(exp)-1]).isalnum() == False or str(exp[0]).isalnum() == False:
      return False
    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           