def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return '0D'
    elif len(palabra1)==len(palabra2):
        n=0
        m=0
        for letra in palabra1:
            if letra==palabra2[n]:
                n=n+1
            elif letra!=palabra2[n]:
                n=n+1
                m=m+1
        if m==1:
            return '1S'
        else:
            return '+1'
    elif len(palabra1)-len(palabra2)>=2 or len(palabra2)-len(palabra1)>=2:
        return '+1'
    elif (len(palabra1)-len(palabra2))==1:
        l=0
        p=0
        for letra in palabra1:
            palabra2=palabra2+' '
            if letra==palabra2[l]:
                l=l+1
            elif letra!=palabra2[l]:
                p=p+1
        if p==1:
            return 'IB'
        else:
            return '+1'
    elif (len(palabra2)-len(palabra1))==1:
        q=0
        r=0
        for letra in palabra2:
            palabra1=palabra1+' '
            if letra==palabra1[q]:
                q=q+1
            elif letra!=palabra1[q]:
                r=r+1
        if r==1:
            return 'IB'
        else:
            return '+1'