def jerigonzo(string):
    jer = ''
    for letra in string:
        if letra in 'AEIOUaeiou':
            jer += letra
            jer += 'p'
        jer += letra
    return jer
if __name__ == "__main__":
    pass
         