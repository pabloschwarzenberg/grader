def buscarTodas(a,b):
    encuentra=""
    num=0
    for i in a:
        if i == b:
            if encuentra == "":
                strnumero = str(num)
                encuentra = encuentra + strnumero
                num = num + 1
            else:
                encuentra= encuentra+" "
                strnumero = str(num)
                encuentra = encuentra + strnumero
                num = num + 1
        else:
            num=num+1
    return encuentra