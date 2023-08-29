def jerigonzo(string):
    lista1=["a","e","i","o","u"]
    lista2=["apa","epe","ipi","opo","upu"]
    s=list(string)
    i=0
    j=0
    while i<len(s):
        if s[i]==lista1[j]:
            s[i]==lista2[j]
        if j<4:
            j=j+1
        if j==4:
            i=i+1
            j=0
    string="".join(s)           
    return string

if __name__ == "__main__":
    pass
         