def rot13(palabra):
    a=''
    for i in palabra:
        b=ord(i)
        if 65<=b<=77:
            a+=chr(b+13)
        elif 78<=b<=90:
            a+=chr(b-13)
        elif 97<=b<=109:
            a+=chr(b+13)
        elif 110<=b<=122:
            a+=chr(b-13)
        else:
            a+=i
    return a