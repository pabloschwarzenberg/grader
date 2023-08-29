def levenshtein(palabra1, palabra2):
    if palabra1==palabra2:
        return "0D"
    elif len(palabra1)-len(palabra2)>1 or len(palabra2)-len(palabra1)>1:
        return "+1"
    elif len(palabra1)>len(palabra2):
        aux=0
        for i in range(len(palabra2)):
            if aux>1:
                return "+1"
                break
            if palabra2[i]==palabra1[i+aux]:
                aux+=0
            else:
                aux+=1
                i-=1
        if aux<=1:
            return "IB"
            
    elif len(palabra2)>len(palabra1):
        aux=0
        for i in range(len(palabra1)):
            if aux>1:
                return "+1"
                break
            if palabra2[i+aux]==palabra1[i]:
                aux+=0
            else:
                aux+=1
                i-=1    
        if aux<=1:
            return "IB"
            
    elif len(palabra1)==len(palabra2):
        aux=0
        for i in range(len(palabra2)):
            if palabra2[i]==palabra1[i]:
                aux+=0
            else:
                aux+=1
        if aux==1: 
          return "1S"
        else: 
          return "+1"
if __name__=="__main__":
    pass

           