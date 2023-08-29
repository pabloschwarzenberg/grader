#ACCTGGTTCTGTAGTCAGGATTACTA 
#___TG_______A__C_G__TT_C_AGTAGTCGATT
#   TG       A  C G  TT C AGTAGTCGATT

string1=input()
string2=input()
lista1=list(string1)
lista2=list(string2)
alineado=[]
i=0
j=0

for n in lista1:
    while i<len(string1):
        if string1[i]!=string2[j]:
            alineado.insert(i,"_")
            i+=1
        else:
            alineado.insert(i,string2[j])
            i+=1
            j+=1

letras = alineado.count("A")+alineado.count("T")+alineado.count("C")+alineado.count("G")
resto=string2[letras:len(string2)]
alineado.append(resto)
        
string22="".join(alineado)
print(string22)