def decodificar(m):
    m = m.split(",")
    p_c = []
    for i in m:
        ci = 0 
        e = 7
        for k in i:
            op = 2 ** e
            if k == "0":
                ci += 0
            else:
                ci += op
            e -= 1
        l = chr(ci)
        p_c.append(l)
        m = "".join(p_c)
    return m

if __name__ == "_main_":
    m=decodificar("01101000,01101111,01101100,01100001")
    print(m)