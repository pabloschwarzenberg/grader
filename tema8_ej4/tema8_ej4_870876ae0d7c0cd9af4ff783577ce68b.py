def rot13(palabra):
    upper_part = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    lower_part = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    palabra_codificada = []
    i = 0
    upper = 'abcdefghijklm'
    lower = 'nopqrstuvwxyz'
    while i < len(palabra):
        if bool(palabra[i] in upper_part) == True:
            x = upper.find(palabra[i])
            palabra_codificada.append(lower_part[x])
        elif bool(palabra[i] in lower_part) == True:
            x = lower.find(palabra[i])
            palabra_codificada.append(upper_part[x])
        i = i+1
    return ''.join(palabra_codificada)