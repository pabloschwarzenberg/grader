def rot13(p):
    x =""
    p_1 = p.lower()
    l = "abcdefghijklmnopqrstuvwxyz"
    l_1 = "nopqrstuvwxyzabcdefghijklm"
    for i in p_1:
        if i in l:
            pos = l_1[l.find(i)]
            x = x + pos
    return x