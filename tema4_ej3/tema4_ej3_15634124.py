vocales = ["a","e","i","o","u"]
def jerigonzo(string):
    s1=list(string)
    i=-1
    while i<len(s1)-1:
        i=i+1
        if s1[i] in vocales:
            s1[i]=s1[i]+"p"+s1[i]
        else: 
            continue
        
    b="".join(s1)
    return b
if __name__ == "__main__":
    pass
         