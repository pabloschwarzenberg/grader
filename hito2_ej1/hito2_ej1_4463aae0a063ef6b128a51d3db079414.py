def prespacedown(a1,b1):
    a1s="".join(a1)
    b1s="".join(b1)
    numa1=0
    numb1=0
    while numa1<len(a1) and numb1<len(b1):
        if a1[numa1]!=' ' and b1[numb1]!=' ':
            if a1[numa1]!=b1[numb1]:
                here=numa1
                break
        numa1+=1
        numb1+=1
    a1s=a1s[here:]
    b1s=b1s[here:]
    return a1s.find(b1s[0])

def prespaceup(b2,a2):
    a2s="".join(a2)
    b2s="".join(b2)
    b2o=b2s
    numa2=0
    numb2=0
    while numa2<len(a2) and numb2<len(b2):
        if a2[numa2]!=' ' and b2[numb2]!=' ':
            if a2[numa2]!=b2[numb2]:
                here=numa2
                break
        numa2+=1
        numb2+=1
    a2s=a2s[here:]
    b2s=b2s[here:]
    if b2s==b2o:
        return 100
    else:
        return a2s.find(b2s[0])

def preasterism(a3,b3):
    while a3[0]==b3[0]:
        a3.pop(0)
        b3.pop(0)
    k=0
    while k<len(a3) and a3[k]!=b3[k]:
        k+=1
    return k

def alinear(ref,lign):
    ref=list(ref)
    lign=list(lign)
    nucleots=len(lign)
    n=0
    while n<nucleots:
        nucli=lign[n]
        nucre=ref[n]
        if nucli!=nucre:
            s_up=prespaceup(ref,lign)
            s_down=prespacedown(ref,lign)
            ast=preasterism(ref,lign)
            if s_down==min(s_up,s_down,ast):
                lign.insert(n,' ')
            elif ast==min(s_up,s_down,ast):
                lign.pop(n)
                lign.insert(n,'*')
            elif s_up==min(s_up,s_down,ast):
                ref.insert(n,' ')
        n+=1
    return ref,lign
if __name__=="__main__":
    seq1=input("Ingrese secuencia 1: ")
    seq2=input("Ingrese secuencia 2: ")
    print("".join(alinear(seq1,seq2)[0]))
    print("".join(alinear(seq1,seq2)[1]))