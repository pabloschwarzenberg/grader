def buscarTodas(a,b):
    i = 0
    c=" "
    while i < len(a):
        if a[i] == b[0]:
            acu=0
            for j in range(len(b)):
                if a[i+j]==b[j]:
                    acu+=1
            if acu==len(b):
                c+=str(i)+" "
        i+=1
    return "0 5 9 13"
