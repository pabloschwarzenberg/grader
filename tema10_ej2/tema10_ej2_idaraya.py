def levenshtein(x,y):
    if x==y:
        print ("Todo perfect: 0")
        return "0D"
    else:
        if len(x)==len(y):
            contador=0
            for i in range(len(x)):
                if x[i]!=y[i]:
                    contador+=1
            print ("Remplace ", contador, "caracteres")
            if contador==1:
                return "1S"
        else:
            z=list(y)
            for i in range(len(x)):
                if x[i] in z:
                    z.remove(x[i])
            if abs(len(x)-len(y))==len(z):
                print ("Agregue/quite: ", len(z), "caracteres")
                if len(z)==1:
                    return "IB"
                elif len(z)>1:
                    return "+1"
            else:
                print ("Operacion mixta")
                return "+1"


if __name__=="__main__":

    levenshtein("jarron", "melon")
    
  
           
