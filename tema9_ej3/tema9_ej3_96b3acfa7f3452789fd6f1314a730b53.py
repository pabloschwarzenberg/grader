def decodificar(m):
    m = m.split(",")
    p_c = []
    for i in m:
        c = 0 
        e = 7
        for k in i:
            op = 2 ** e
            if k == "0":
                c += 0
            else:
                c += op
            e -= 1
        l = chr(c)
        p_c.append(l)
        m = "".join(p_c)
    return m

if __name__ == "main":
    m=decodificar("01101000,01101111,01101100,01100001")
    print(m)