def jerigonzo(palabra):
    traduccion = ''
    for letra in palabra:
        if letra in 'A,E,I,O,U,a,e,i,o,u':
            traduccion += letra
            traduccion += 'p'
        traduccion += letra
    return traduccion

if __name__ == "__main__":
    pass