def funcion(p1, p2):
   
    
    if len(p2) == 0:
        return len(p1)
        
    if len(p1)<len(p2):
        return funcion(p2,p1)
    fila_anterior = range(len(p2)+1)
    for i, c1 in enumerate(p1):
        fila_actual = [i+1]
        for j, c2 in enumerate(p2):
            insertions = fila_anterior[j+1] + 1
            deletions = fila_actual[j] + 1
            substitutions = fila_anterior[j] +(c1!=c2)
            fila_actual.append(min(insertions,deletions,substitutions))
        fila_anterior = fila_actual
    
    return fila_anterior[-1]
  
def levenshtein(p1,p2):
    if funcion(p1,p2) == 0:
        return "0D"
    elif funcion(p1,p2) == 1:
        if len(p1) == len(p2):
            return"1S"
        else:
            return "IB"
    elif funcion(p1,p2) > 1 : 
        return "+1"
    
   
if __name__=="__main__":

    p1 = input()
    p2 = input()
  
    
    
           