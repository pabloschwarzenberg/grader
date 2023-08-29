vocales="aeiou"
def jerigonzo(string):
    cambio="p"
    s=""
    i=0
    while i<len(string):
        s=s+string[i]
        if string[i]==vocales[0]:    
            s=s+cambio+string[i]
        if string[i]==vocales[1]:
            s=s+cambio+string[i]
        if string[i]==vocales[2]:
            s=s+cambio+string[i]
        if string[i]==vocales[3]:
            s=s+cambio+string[i]
        if string[i]==vocales[4]:
            s=s+cambio+string[i]
        
        i=i+1
    return s.lower()
    return string

if __name__ == "__main__":
    pass
         