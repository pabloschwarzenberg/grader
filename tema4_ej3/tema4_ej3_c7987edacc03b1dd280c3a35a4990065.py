def jerigonzo(string):
    string = [c for c in string]
    for ix in range(len(string)):
        if string[ix] in 'aeiou':
            string[ix] = string[ix] + 'p' + string[ix]
    return ''.join(string)


if __name__ == '__main__':
    print(jerigonzo(input('Escriba una palabra para convertirla a jerigonzo: ')))