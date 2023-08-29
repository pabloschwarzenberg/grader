def jerigonzo(string):
    a=string
    a=list(a)
    for j in range(0,len(a)):
        for r in ["a","e","i","o","u"]:
            if (a[j]==r):
                a[j]=a[j]+"p"+a[j]
    return("".join(a))

if __name__ == "__main__":
    pass
         