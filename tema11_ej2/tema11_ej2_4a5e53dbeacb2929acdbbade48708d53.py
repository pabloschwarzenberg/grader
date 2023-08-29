def validar_expresion(e):    
  if(len(e)==1):
      if(e[0] in "1234567890"):
       return True
      if(e[0]=="+" or e[0]=="-"):
       return False
  lista=[e[0]]
  a=list(e)
  a.pop(0)  
  e="".join(a)  
  if(e[0] in "1234567890"):
      if(lista[0]!="+" and lista[0]!="-"):
          return False
  if(e[0]=="+" or e[0]=="-"):
      if(lista[0] not in "1234567890"):
          return False 
  return validar_expresion(e)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           