def levenshtein(s1,s2):
    if s1 == s2:
        return '0D'
    else:
        if len(s1)>len(s2):
            DIF = len(s1)-len(s2)
            if DIF == 0:
                return 'IB'
            else:
                return '+1'
        elif len(s1)<len(s2):
            DIF = len(s2)-len(s1)
            if DIF == 1:
                return 'IB'
            else:
                return '+1'
            return 'IB'
        else:
            DIF = 0
            c = 0
            c2 = 0
            for x in s1:
                if x != s2[c]:
                    c2+=1
                c+=1
            if c2 == 1:
                return '1S'
            else:
                return '+1'
        if DIF > 1:
            return '+1'         