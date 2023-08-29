def levenshtein(palabra1,palabra2):
    print(len(palabra1))
    print(len(palabra2))
    if len(palabra1)!=len(palabra2):
        cantidad_de_letras1=len(palabra1)
        cantidad_de_letras2=len(palabra2)
        distancia=cantidad_de_letras1-cantidad_de_letras2
        print(distancia)
        if distancia>1 or distancia<-1:
            print("+"+str(1))
            return "+"+str(1)
        if distancia==1 or distancia==-1:
          if palabra1[0]!=palabra2[0]:
            print("+1")
            return "+"+str(1)
          if palabra1[0]==palabra2[0]:
            print(str(1)+"o"+str(-1))
            return "IB"
          
    if len(palabra1)==len(palabra2):
        if palabra1==palabra2:
            print("0D")
            return "0D"
        if palabra1!=palabra2:
            i=0
            while i<=len(palabra1):
                if palabra1[i]==palabra2[i]:
                    i=i+1
                if palabra1[i]!=palabra2[i]:
                    p2=palabra2.replace(palabra2[i],palabra1[i])
                    print(palabra1)
                    print(p2)
                    return "1S"
                    
                    