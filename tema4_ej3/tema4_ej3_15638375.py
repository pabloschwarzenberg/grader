def jerigonzo(a):
    i=0
    while i < len(a):
        if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
            a=a[:i+1]+'p'+a[i]+a[i+1:]
            i+=3
        else:
            i+=1
    return a

if __name__ == "__main__":
    pass
         