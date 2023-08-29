def alinear(string1,string2):
    i = 0
    resultado = ""
    j = 0
    while i<len(string1):
        if string1[i]==string2[j]:
            resultado+=string2[j]
            j+=1
        else:
            resultado += "_"
        i+=1
    resultado += string2[j:]
    return resultado

string1 = input("")
string2 = input("")
print (alinear(string1,string2))