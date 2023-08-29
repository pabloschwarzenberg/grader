def levenshtein(s, t):
    if s == t:
        return "0D"
    if abs(len(s) - len(t)) > 1:
        return "+1"
    if len(s) > len(t):
        s, t = t, s
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i:] == t[i + 1:]:
                return "IB"
            elif s[i + 1:] == t[i + 1:]:
                return "1S"
            elif s[i + 1:] == t[i:]:
                return "IB"
            else:
                return "+1"
    return "IB"
