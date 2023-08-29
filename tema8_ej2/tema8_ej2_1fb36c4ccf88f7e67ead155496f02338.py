def buscarTodas(a,b):
    out_str = ""
    rindex = 0
    while b in a:
        pos1 = a.find(b)
        out_str += str(pos1+rindex)+" "
        nindex = pos1+len(b)
        rindex += pos1 +len(b)
        a = a[nindex:]
        print(a)
        
    return out_str.strip()

if __name__ == "__main__":
    pass
           