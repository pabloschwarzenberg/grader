def buscarTodas(a,b):
    lugares = ''
    num = 0
    for i in a:
        if i == b:
            if lugares == '':
                strnum = str(num)
                lugares = lugares+strnum
                num = num+1

            else:
                lugares = lugares+''
                strnum = str(num)
                lugares = lugares+" "+strnum
                num = num+1

        else:
            num = num+1
    return lugares