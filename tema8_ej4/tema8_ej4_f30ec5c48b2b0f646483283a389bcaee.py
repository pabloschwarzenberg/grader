def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )


# In[ ]:


def buscarTodas(a,b):
    lista =[]
    s=" "
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(str(i))
            l=s.join(lista)
            if(len(lista)==0):
                return "no existe"
    return l