def rot13(palabra):
    palabra=list(palabra)
    palabra_num = len(palabra)
    Ascii=""
    for x in range(0,palabra_num):
        ASCII= ord(palabra[x])
        if ASCII<110:
            ASCII= ASCII+13
        else:
            ASCII= ASCII-13
        Ascii+=chr(ASCII)
        ASCII=0    
    return Ascii
