def levenshtein(palabra1,palabra2):
    l1=list(palabra1)
    l2=list(palabra2)
    if l1==l2:
        return "0D"
    if len(palabra1)==len(palabra2):
        cambios=[]
        i=0
        while i<len(l1):
            if l1[i]==l2[i]:
                l1.pop(i)
                l2.pop(i)
            else:
                cambios.append([l1[i],l2[i]])
                i=i+1
        if len(cambios)==1:
            return "1S"
        else:
            return "+1"
    else:
        if len(palabra1)+1==len(palabra2):
            cambios=0
            i=0
            while i<len(l2):
                if l1[i]==l2[i]:
                    i=i+1
                else:
                    cambios+=1
                    l2.pop(i)
            if cambios==1:
                return "IB"
            else:
                return "+1"
        if len(palabra1)==len(palabra2)+1:
            cambios=0
            i=0
            while i<len(l1):
                if l1[i]==l2[i]:
                    i=i+1
                else:
                    cambios+=1
                    l1.pop(i)
            if cambios==1:
                return "IB"
            else:
                return "+1"
        else:
            return "+1"
if __name__=="__main__":
  palabra1=input("Palabra 1?: ")
  palabra2=input("Palabra 2?: ")
  print(levenshtein(palabra1,palabra2))