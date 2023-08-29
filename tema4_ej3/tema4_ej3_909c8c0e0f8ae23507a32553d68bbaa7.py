def jerigonzo(string):
    a=list(string)
    b=[i for i, x in enumerate(a) if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u")]
    c=[x+1 for x in b]
    j=0
    n=0
    while j < len(c):
        a.insert((c[j]+n), "px")
        j+=1
        n+=1
    for u in range(0,len(a)):
        if a[u-1] == "a":
             a[u] = "pa"
        elif a[u-1] == "e":
             a[u] = "pe"
        elif a[u-1] == "i":
             a[u] = "pi"
        elif a[u-1] == "u":
             a[u] = "pu"
        elif a[u-1] == "o":
             a[u] = "po"
        u+=1
    d="".join(a)
    return d

if __name__ == "__main__":
    pass
         