def buscarTodas(a,b):
    c=len(a)


    i = 0

    j = []
    while (i < c):
        if(a[i]==b):
            j.append(i)
            i = i + 1
        else:
            i=i+1

    print(j)
    n=str(j)
    r=n.replace("[","").replace(",","").replace(",","").replace(",","").replace("]","")



    return(r)

           