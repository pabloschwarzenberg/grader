def validar_expresion(w):
  if w[-1]=='-' or w[-1]=='+' :
      return False
  for i in range(1,len(w)):
      z=list(w)
      n=['1','2','3','4','5','6','7','8','9','0']
      s=['+','-']
      if s.count(z[i])==1:
          if s.count(z[i-1])==1:
              return False
            
          elif n.count(z[i-1])==1:
              z.remove(z[i])
              validar_expresion(''.join(z))
              return True
      elif n.count(z[i])==1:
          if n.count(z[i-1])==1:
              return False
            
          elif s.count(z[i-1])==1:
              z.remove(z[i])
              validar_expresion(''.join(z))
              return True          
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
  