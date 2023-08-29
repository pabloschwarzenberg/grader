def levenshtein(palabra1,palabra2):
    str1="+1"
    str2="IB"
    str3="1S"
    str4="0D"
    numero=len(palabra1)-len(palabra2)

    if numero==0:
        if palabra1==palabra2:
            return str4
        else:
            contador=0
            for i in range(0,len(palabra1)):
                           a=palabra1[i]
                           b=palabra2[i]
                           if a!=b:
                                    contador=contador+1
            if contador==1:                          
                           return str3
            else:
                           return str1

                           
    if numero!=0:
        if numero==1:
            contador=0
            for i in range(0,len(palabra2)):
                           a=palabra1[i]
                           b=palabra2[i]
                           if a!=b:
                                    contador=contador+1
            if contador==0:
                           return str2
            if contador>0:
                           return str1
            if contador==1:
                return str2
        if numero==-1:
            contador=0
            for i in range(0,len(palabra1)):
                           a=palabra1[i]
                           b=palabra2[i]
                           if a!=b:
                                    contador=contador+1
            if contador==0:
                           return str2
            if contador>0:
                for j in range(0,len(palabra2)):
                    c=palabra1
                    d=palabra2.replace(palabra2[j],"",1)
                    if c==d:
                        return str2

                           

        elif numero>1 or numero<-1:
            return str1