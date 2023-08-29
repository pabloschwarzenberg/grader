M="L"

def levenshtein(palabra1, palabra2):
    r1=list(palabra1)
    r2=list(palabra2)
    for n in range(len(r1)-1):
        if r1[n]!=r2[n] and r1[n]!=M and len(r1)==len(r2) or len(r2)-len(r1)>1 and r1[n]==r2[n] or r1[n]!=r2[n] and len(r1)-len(r2)>1 or len(r1)-len(r2)>=1: 
           return ("+1")
        elif palabra1==palabra2:
             return ("0D")
        else:
             if len(r1)-len(r2)==-1 or len(r2)-len(r1)==1 and r1[n]!=r2[n] or len(r1)!=len(r2) and r1[n]==r2[n]:
               return ("IB")
             else:
                   return("1S")
             
       
             
          
