def mcm(p,q,pq):
    if p<q:
        return mcm(q,p,pq)
    elif q==0:
        return p
    else:
        return mcm(q,p%q,pq)

if __name__=="__main__":
    p=int(input())
    q=int(input())
    pq=p*q
    print(pq/mcm(p,q,pq))
           