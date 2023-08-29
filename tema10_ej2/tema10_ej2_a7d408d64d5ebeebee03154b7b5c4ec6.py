def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return "0D"
    else:
        if len(palabra1)==(len(palabra2)-1):
            i=0
            while i<len(palabra1):
                if palabra2.find(palabra1[i])!=-1:
                    return "IB"
                else:
                    return "+1"
        elif (len(palabra1)-1)==len(palabra2):
            i=0
            while i<len(palabra2):
                if palabra1.find(palabra2[i])!=-1:
                    return "IB"
                else:
                    return "+1"
        elif len(palabra1)==len(palabra2):
            contar=[]
            i=0
            while i<(len(palabra2)):
                c=palabra2[i]
                if palabra1.find(c)!=-1:
                    contar.append(1)
                    palabra1=palabra1.replace(palabra2[i],"",1)
                i+=1
            if len(contar)==(len(palabra2)-1):
                return "1S"
            elif len(contar)<(len(palabra2)-1):
                return "+1"
        else:
            return "+1"        

if __name__=="__main__":
    palabra1=input()
    palabra2=input()
    print(levenshtein(palabra1,palabra2))