def validar_expresion(expresion):
   operandores=[]
   operandos=[]
   a=expresion
   signos=["+","-"]
   for i in range (len(a)):
     if a[i] in signos:
       operandores.append(a[i])
     else:
       operandos.append(a[i])
   if len(operandos)<=len(operandores):
     return False
   else:
     return True
   

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           