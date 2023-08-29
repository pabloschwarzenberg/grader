def validar_expresion(expresion):
    numeros="1234567890"
    i=1
    while i<len(expresion):
      if len(expresion)>2:
          if expresion[i]=="+" or expresion[i]=="-":
            if numeros.find(expresion[i-1])!=-1 and numeros.find(expresion[i+1])!=-1:
              return True
            else:
              return False
          else:
            return False
      else:
        return False
 

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           