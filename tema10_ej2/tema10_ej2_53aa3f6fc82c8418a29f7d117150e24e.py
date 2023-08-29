
def levenshtein(palabra1,palabra2):
    y=list(palabra1)
    z=list(palabra2)
    a=len(y)
    s=len(z)
    q=0
    m=len(set(y) & set(z))
    if a==s:

        if palabra1==palabra2:
               return ('0D')
        else:
            for x in range(a):
                if y[x]!=z[x]:
                    q=q+1
            if  q==1:
                return ('1S')
            elif q>1:
                return ('+1')
    else:
        if a>s:
            for x in range(a):
                if y[x]==y[x]:
                    q=q+1
            if s==m:
                if q-m == 1:
                    return 'IB'
                elif q-m > 1:
                    return '+1'
            elif m<s:
                if q-m >= 1:
                    return '+1'
        elif s>a:
            for x in range(s):
                if z[x]==z[x]:
                    q=q+1
            if a==m:
                if q-m==1 :
                    return 'IB'
                elif q-m > 1:
                    return '+1'
            elif m<a:
                if q-m >= 1:
                    return '+1'
