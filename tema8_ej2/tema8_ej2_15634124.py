def buscarTodas(a,b):
    s1=list(a)
    s2=list(b)
    sf=[]
    i=0
    j=0
    sub = s2
    if any(sub in string for string in s1): 
        return "\n".join(s2 for sub in s1 if sub in s2)
        
if __name__ == "__main__":
    pass
           