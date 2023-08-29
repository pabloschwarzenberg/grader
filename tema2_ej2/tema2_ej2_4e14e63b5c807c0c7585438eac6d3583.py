def amigos(n1,n2):
    div1=[]
    div2=[]
    cont=1
    while cont< n1:
        if n1%cont ==0:
            div1.append(cont)
        if n2%cont ==0:
            div2.append(cont)
        cont=cont+1

    sum1=sum(div1)
    sum2=sum(div2)
    if(sum1==n2 and  sum2 ==n1):
        return True
    else:
        return False