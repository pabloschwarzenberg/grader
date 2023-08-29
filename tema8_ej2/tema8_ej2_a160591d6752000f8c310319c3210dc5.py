def buscarTodas(a,b):
    result=""
    strInt=0

    for i in a:
        if i==b:
            num=str(strInt)
            if strInt<len(a):
                result+=num+" "
        strInt+=1
    return result          