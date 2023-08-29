def jerigonzo(string):
    traducida = ''
    for i in string:
        traducida += i
        if 'aeiou'.find(i) != -1:
            traducida += 'p' + i
    return traducida

if __name__ == "__main__":
    pass
         