def validar_expresion(expresion):
    try:
      a = int(expresion[0])
      b = int(expresion[2])
      c = str(expresion[1])
      if c == "+":
        d = a + b
      elif c == "-":
        d = a - b  
    except: 
      return False
    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           