def validar_expresion(expresion,j=0,i=0):
  if isinstance(expresion,list)==False:
     expresion=list(expresion)
  a=len(expresion)-1
  h=expresion[a]
  if h.isdigit()==True:
         i=i+1
  elif h=="+" or h=="-":
         j=j+1
  expresion.pop(a)
  if expresion==[]:
      if j==(i-1):
       digito=[]
       otro=[]
       return True
      elif j<=i-1 or i==j or j>i:
       digito=[]
       otro=[]
       return False
  else:
    return(validar_expresion(expresion,j,i))

     
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))