def jerigonzo(string):
    e=len(string)
    string=string.lower()
    v=["a","e","i","o","u"]
    r=[]
    for i in range(e):
        if string[i] in v:
            r.append(string[i])
            r.append("p")
            r.append(string[i])            
        else:
            r.append(string[i])
    r="".join(r)
    return r
    

if __name__ == "__main__":
    pass
         