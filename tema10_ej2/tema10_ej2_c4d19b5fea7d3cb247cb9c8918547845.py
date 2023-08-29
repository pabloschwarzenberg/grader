def levenshtein(palabra1,palabra2):

    d =[]
    der = []
    h=[]

    if(len(palabra1)>len(palabra2)):

        for i in range(len(palabra2)):

            k = palabra1.count(palabra2[i])
            no = palabra2.count(palabra2[i])


            if(k == no):

                continue

            else:

                l = abs(k-no)
                d.append(l)
        z = d
        for tr in range(len(d)):

            if tr not in range(len(d)):

                break

            elif (z.count(z[tr]) > 1):

                z.pop(tr)

            else:

                continue
        
        if(len(palabra1)-len(palabra2)>=1):
            rt = len(palabra1)-len(palabra2)
            po = sum(d[0:])+ rt

        else:

            po = sum(d[0:])


        if(po > 1):

            bf = "+1"

        elif(po == 1):

            bf = "IB"


        elif(po == 0):

            bf = "0D"


    elif(len(palabra2) == len(palabra1)):

        for i in range(len(palabra2)):

            k = palabra1.count(palabra2[i])
            no = palabra2.count(palabra2[i])
            g = k,no
            g = list(g)


            if (k == no):

                continue

            else:

                d.append(g)

        f = d

        for x in range(len(d)):

            if x not in range(len(d)):

                break

            elif(f.count(f[x])>1):

                f.pop(x)

            else:

                continue




        y = 0
        while y < len(f):

            x = abs(f[y][0]-f[y][1])
            der.append(x)
            y = y+1


        po = sum(der[0:])

        if(der.count(0)>=1):

            if(po == 1):

                bf = "IB"


        elif (po > 2):

            bf = "+1"

        elif (po <= 2 and po > 0):

            bf = "1S"


        elif (po == 0):

            bf = "0D"




    elif(len(palabra1)<len(palabra2)):

        for r in range(len(palabra1)):

            k = palabra1.count(palabra1[r])
            no = palabra2.count(palabra1[r])
            g = k, no
            g = list(g)


            if (k == no):

                continue

            else:

                d.append(g)


        z = d


        for tr in range(len(d)):

            if tr not in range(len(d)):

                break

            elif (z.count(z[tr]) > 1):

                z.pop(tr)

            else:

                continue


        y = 0

        while y < len(z):

            x = abs(z[y][0] - z[y][1])
            h.append(x)
            y = y + 1

        if(len(palabra2)-len(palabra1)>1):
            rt = len(palabra2)-len(palabra1)
            po = sum(h[0:])+ rt

        else:

            po = sum(h[0:])

        

        if (po > 1):

            bf = "+1"

        elif (po == 1):

            bf = "IB"


        elif (po == 0):

            bf = "0D"





    

    return  bf
 

if __name__=="__main__":
    palabra1 = str(input("Ingrese palabra 1: "))
    palabra2 = str(input("Ingrese palabra 2: "))
    
           