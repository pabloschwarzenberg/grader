palabra = input(str('Ingrese una palabra:'))

def rot13(palabra):
    result = ""

    for i in palabra:
        x = ord(i)
        if x >= ord('a') and x <= ord('z'):
            if x > ord('m'):
                x -= 13
            else:
                x += 13
        elif x >= ord('A') and x <= ord('Z'):
            if x > ord('M'):
                x -= 13
            else:
                x += 13
        result += chr(x)
    return result

print(rot13(rot13(palabra)))
print(rot13(palabra))




