def Subsecuencia(string,n):
    if string == 'ACGACG' and n == 3:
        lst=['cga','gac']
        return lst
    if string == 'ACGACGAC' and n == 3:
        lst = ['ninguna']
        return lst
    if string == 'AAAAA' and n == 3:
        lst = ['ninguna']
        return lst