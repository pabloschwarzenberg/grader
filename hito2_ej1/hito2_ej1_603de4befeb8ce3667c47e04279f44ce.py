def Alineamiento(str1,str2):
    alineado = []
    contador = 0
    for i in str1:
        if str2[contador] != i:
            alineado.append("_")
        elif str2[contador] == i:
            alineado.append(i)
            contador = contador + 1
    alineado = "".join(alineado) + str2[contador:]   
    return alineado
#print(Alineamiento("ACCTGGTTCTGTAGTCAGGATTACTA","TGACGTTCAGTAGTCGATT"))
