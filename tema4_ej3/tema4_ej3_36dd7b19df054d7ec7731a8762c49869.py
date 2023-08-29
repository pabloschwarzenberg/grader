def jerigonzo(string):
    vocal = ''
    for i in string:
        if i in 'aeiou':
            vocal += i
            vocal += 'p'
        vocal += i
    return vocal

if __name__ == "__main__":
    pass
         