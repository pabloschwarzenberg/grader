def validar_expresion(expresion):
    if len(expresion) == 1:
      return True
    else:
       a = expresion[0]
       b = expresion[-1]
       if (a.isnumeric() == True and b.isnumeric() == True) or (a.isnumeric() == False and b.isnumeric() == False):
               c = expresion[1:-1]
               return validar_expresion(c)
       else:
           return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           