def validar_expresion(expresion):
    l=list(expresion)
    n=len(l)
    if l[n-1] not in ["0","1","2","3","4","5","6","7","8","9"] or l[0] not in ["0","1","2","3","4","5","6","7","8","9"]:
      return False
    else:
      return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           