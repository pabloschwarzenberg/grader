def rot13(m):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = a[13:]
    c = a[:13]
    w = ""
    for i in range(len(m)):
        if m[i] in b:
            d = b.find(m[i])
            e = c[d]
            w = w + e
        elif m[i] in c:
            f = c.find(m[i])
            g = b[f]
            w = w + g
    return w

if __name__=="__main__":
   n = input("Ingrese palabra:")
   print(rot13(n))
           