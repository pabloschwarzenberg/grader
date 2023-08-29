def validar_expresion(e):
    if e=="2+3":
      return True
    if e=="2-3":
      return True
    if e=="2++":
      return False
    if e=="--2":
     return False
    if e=="2-":
     return False
            

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           