# completa el código de la función
def amigos(a,b):
        s1 = []
        s2 = []
        sDIVa = 0
        sDIVb = 0
        for i in range(a) :
                if(a%(i+1) == 0) :
                        s1.append(i+1)
                i = i + 1
        for i in s1 :
                sDIVa = sDIVa + i
                
        for i in range(b) :
                if(b%(i+1) == 0) :
                        s2.append(i+1)
                i = i + 1
        for i in s2 :
                sDIVb = sDIVb + i
        if(sDIVa == sDIVb and a != b) : es = True
        else : es = False
        print(sDIVa,sDIVb)
        return(es)


           