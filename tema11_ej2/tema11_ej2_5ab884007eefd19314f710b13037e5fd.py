def validar_expresion(expresion):
  expresion=list(expresion)
  if expresion[0]=="+" or expresion[0]=="-":
    return False
  else:
    return validar(expresion,expresion[0])
  
def validar(expresion,n):
  expresion.pop(0)
  num=["0","1","2","3","4","5","6","7","8","9"]
  exp=["+","-"]
  if len(expresion)==0 and (n in num):
    return True
  if len(expresion)==0 and (n not in num):
    return False
  else:
    if n in num:
      if expresion[0] in exp:
        return validar(expresion,expresion[0])
      else:
        return False
    if n in exp:
      if expresion[0] in num:
        return validar(expresion,expresion[0])
      else:
        return False
        
      

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           