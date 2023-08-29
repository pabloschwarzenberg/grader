def rot13(palabra):
    L=[["a","b","c","d","e","f","g","h","i","j","k","l","m"],["n","o","p","q","r","s","t","u","v","w","x","y","z"]]
    l=list(palabra)
    for i in range(len(palabra)):
        for j in range(13):
            if l[i]==L[0][j]:
                l[i]=L[1][j]
            else:
                if l[i]==L[1][j]:
                    l[i]=L[0][j]
    palabra1=""
    for k in range(len(palabra)):
        palabra1+=l[k]
    return palabra1