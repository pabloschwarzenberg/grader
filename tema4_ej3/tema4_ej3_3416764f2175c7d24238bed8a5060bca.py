def jerigonzo(texto):

    x = list(texto)
    
    i=0
    
    while i<len(x):

        if x[i]=='a':
            x[i]='apa'

        if x[i]=='e':
            x[i]='epe'

        if x[i]=='i':
            x[i]='ipi'

        if x[i]=='o':
            x[i]='opo'

        if x[i]=='u':
            x[i]='upu'

        i=i+1

    traduccion = ''.join(x)

    return traduccion
         