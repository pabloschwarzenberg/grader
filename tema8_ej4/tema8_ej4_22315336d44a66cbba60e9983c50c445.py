def rot13(a):
    a=a.lower()
    l1 = "abcdefghijklm";
    l2 = "nopqrstuvwxyz";
    c = ""
    for x in a:
        if x in l1:
            r = l1.index(x);
            c += l2[r]
        if x in l2:
            r = l2.index(x);
            c += l1[r]
        if x == " ":
            c += x
    return c