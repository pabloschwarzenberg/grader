def rot13(a):
    a=a.lower()
    l1="abcdefghijklmnopqrstuvwxyz";
    l2="nopqrstuvwxyzabcdefghijklm";
    c=""
    for x in a:
        if x in l1:
            r=l1.index(x);
            c+=l2[r]
        elif x in l2:
            r=l2.index(x);
            c+=l1[r]
        elif x=="":
            c+=x
    return c.lower()
print(rot13("hola"))
           