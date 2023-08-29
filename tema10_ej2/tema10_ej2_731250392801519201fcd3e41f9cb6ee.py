M="L"

def levenshtein(p1,p2):
    l1=list(p1)
    l2=list(p2)
    for i in range (len(l1)-1):
        if l1[i]!=l2[i] and l1[i]!= M and len(l1)==len(l2) or len(l2)-len(l1)>1 and l1[i]==l2[i] or l1[i]!=l2[i] and len(l1)-len(l2)>1 or len(l1)-len(l2)>=1: 
            return("+1")
        elif p1==p2:
             return("0D")
        else:
             if len(l1)-len(l2)==-1 or len(l2)-len(l1)==1 and l1[i]!=l2[i] or len(l1)!=len(l2) and l1[i]==l2[i]:
               return("IB")
             else:
                   return("1S")
           