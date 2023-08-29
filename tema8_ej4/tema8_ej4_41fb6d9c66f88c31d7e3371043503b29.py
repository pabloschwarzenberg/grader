def rot13(palabra):
    mensaje = ""
    for n in palabra:
        if (ord(n) >= 65 and ord(n) <= 90) or (ord(n)>= 97 and ord(n) <= 122):
            if (ord(n) + 13 > 90 and ord(n) + 13 <= 103) or (ord(n) + 13 > 122 and ord(n) + 13<= 135):
                mensaje += chr(ord(n) - 13)
            else:
                mensaje += chr(ord(n) + 13)
    return mensaje