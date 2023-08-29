def evaluar_expresion(expresion,operandores,operandos):
 a=expresion
 if len(a)<=2:
     return int(a)
 else:
     if a[0]=="-":
         a=a.replace(a[0],"")
         a=a.strip()
         contador=0
         c=0
         for i in range (len(a)):
             if a[i]=="+" or a[i]=="-":
                 operandores.append(a[i])
                 operandos.append(a[contador:i])
                 contador=i+1
         operandos.append(a[-(len(a)-contador):])
         if operandores[0]=="+":
             c=int(operandos[0])*(-1)+int(operandos[1])
         if operandores[0]=="-":
             c=int(operandos[0])*(-1)-int(operandos[1])
         d=len(operandos[1])
         s=a.find(operandos[1])
         a=(str(a.replace(a[0:s+d],str(c))))
         return evaluar_expresion(a,[],[])

     else:
         contador=0
         c=0
         for i in range (len(a)):
             if a[i]=="+" or a[i]=="-":
                 operandores.append(a[i])
                 operandos.append(a[contador:i])
                 contador=i+1
         operandos.append(a[-(len(a)-contador):])
         if operandores[0]=="+":
             c=int(operandos[0])+int(operandos[1])
         if operandores[0]=="-":
             c=int(operandos[0])-int(operandos[1])
         d=len(operandos[1])
         s=a.find(operandos[1])
         a=(str(a.replace(a[0:s+d],str(c))))
         return evaluar_expresion(a,[],[])

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))

           