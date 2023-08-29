def decodificar(code):
    codes = code.split(',')
    codes = list (map(lambda x: chr(int(str(x), 2)), codes))
    return '' .join(codes) 
   