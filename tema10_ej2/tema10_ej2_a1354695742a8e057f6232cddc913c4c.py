def levenshtein(s1,s2):
    if s1==s2:
        return "0D"
    elif len(s1)==len(s2):
        n_reemplazar = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                n_reemplazar +=1
        if n_reemplazar >1:
                return "+1"
        else:
            return "1S"
    elif abs(len(s1)-len(s2))==1 :
        if len(s1)>len(s2):
            for i in range(len(s1)):
                if s1[:i]+s1[i+1:]==s2:
                    return "IB"
            return "+1"
        else:
            for i in range(len(s2)):
                if s2[:i]+s2[i+1:]==s1:
                    return "IB"
            return "+1"
    else:
        return"+1"