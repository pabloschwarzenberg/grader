def buscarTodas(a,b):
    num = 0
    index = ""
    for x in a:
        numStr = str(num)
        if x == b:
            if index == "":
                index += numStr
            else:
                index += " "
                index += numStr
        num +=1
    return index