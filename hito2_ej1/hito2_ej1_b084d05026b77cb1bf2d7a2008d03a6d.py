string1 = input()
string2 = input()

def alinement(string1, string2):
    s1 = list(string1.upper())
    s2 = list(string2.upper())
    l = []
    for i in range(0, len(s1)):      
        if s1[i]==s2[0]:
            l.append(s2[0])
            s2 = s2[1:]
        else:
            l.append("_")
    l= "".join(l)
    if len(s2) > 0:
        s2 = "".join(s2)
        l = l + s2
    return(l)
l = alinement(string1, string2) 
print(l)
