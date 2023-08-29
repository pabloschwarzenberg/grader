def levenshtein(a, b):
    if a == b:
        return '0D'
    
    elif len(a) == len(b):
        return '1S'
    
    elif abs(len(a)-len(b)) == 1:
        
        for x in a:
            b = b.strip(x)
        
        if len(b) <= 1:
            return 'IB'
        else:
            return '+1'
       
        
    if abs(len(a)-len(b)) > 1:
        return '+1'

if __name__=="__main__":
    pass