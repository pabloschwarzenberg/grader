def jerigonzo(string):
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    s=list(string)
    srl=s.copy()
    k=0
    sr=""
    v=1
    while k < len(s):
        if s[k] in vocales:
            srl.insert(k+v,"p"+s[k])
            v=v+1
        k=k+1
    for n in srl:
        sr=sr+n
    return sr
if __name__ == "__main__":
    pass