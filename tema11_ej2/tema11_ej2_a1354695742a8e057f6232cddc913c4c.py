def validar_expresion(s):
    if len(s) == 1:
        if s.isdigit():
            return True
        else:
            return False
    elif s[len(s)-1].isdigit() == False:
        return False

    else:
        for i in range(1, len(s)):
            if s[i - 1].isdigit() == False and s[i].isdigit() == False:
                return False

            else:
                if s[i].isdigit() == True and validar_expresion(s[i:]):
                    return True
           