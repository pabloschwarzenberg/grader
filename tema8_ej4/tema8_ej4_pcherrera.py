def rot13(s):
        i=0
        sn=""
        while i<len(s):
            j=ord(s[i])
            p=ord(s[i])+13
            if j==32:
                p=32
            if j>=97 and j<=122:
                if p>122:
                    p=p%122
                    if p==0:
                        p=122
                    else:
                        p+=96
            elif j>=65 and j<=90:
                if p>90:
                    p=p%90
                    if p==0:
                        p=90
                    else:
                        p+=64
            q=chr(p)
            sn+=q
            i+=1
        return sn