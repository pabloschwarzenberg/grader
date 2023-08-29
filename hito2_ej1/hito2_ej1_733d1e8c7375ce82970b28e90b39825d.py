def alinearSecuencias(string1,string2):
    string2=list(string2)
    STRING=""
    x=0
    for i in string1:
        if string2[x] == i:
            STRING+=string2[x]
            string2[x]="*"
            x+=1
        else:
            STRING+="_"
    for i in string2:
        if i != "*":
            STRING+=i
    return STRING

#ENTRADA        
s1="ACCTGGTTCTGTAGTCAGGATTACTA"
s2="TGACGTTCAGTAGTCGATT"
#SALIDA
alineado=alinearSecuencias(s1,s2)
print(alineado)