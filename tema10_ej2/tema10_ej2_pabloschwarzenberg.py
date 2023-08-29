def levenshtein(palabra1,palabra2):
    if len(palabra1)==len(palabra2):
        n=0
        for i in range(len(palabra1)):
            if palabra1[i]!=palabra2[i]:
                n+=1
        if n==0:
            return "0D"
        elif n==1:
            return "1S"
        else:
            return "+1"

    else:
        i=0
        j=0
        n=0
        while i<len(palabra2):
            if palabra1[j]==palabra2[i]:
                i+=1
                j+=1
            else:
                n+=1
                i+=1

        if n==1:
            return "IB"
        else:
            return "+1"

if __name__=="__main__":
    print(levenshtein("ola","Hola"))
