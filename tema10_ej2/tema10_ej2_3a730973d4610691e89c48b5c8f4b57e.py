def levenshtein(palabra1,palabra2):

    if len(palabra1)>len(palabra2):
        j=0
        for i in range (0,len(palabra2)):
           if palabra1[i]!=palabra2[i]:
             j=j+1
             
        a=len(palabra1)-len(palabra2)
           
       

        if a==1 and j==0:
           return "IB"
           
        if a==0 and j==1:
           return "IB"
           
        if a==1 and j==2:
           return "IB"
           
        if a==2 and j==1:
           return "+1"

        if j>2 and a>2:
           return "+1"
           
        if j>2 and a==1:
           return "+1"
           
        
    


    if len(palabra1)<len(palabra2):
        j=0
        for i in range (0,len(palabra1)):
           if palabra1[i]!=palabra2[i]:
             j=j+1
             
        a=len(palabra2)-len(palabra1)
       

        
        if a==1 and j==0:
           return "IB"
           
        if a==0 and j==1:
           return "IB"
           
        if a==1 and j==2:
           return "IB"
           
        if a==2 and j==1:
           return "+1"

        if j>2 and a>2:
           return "+1"
           
        if j>2 and a==1:
           return "+1"
    
        





    if len(palabra1)==len(palabra2):
        i=0
        while i<len(palabra1):
            if palabra1[i]!=palabra2[i]:
                return "1S"
                break
            if palabra1[i]==palabra2[i]:
                i=i+1
        return "0D"
      

