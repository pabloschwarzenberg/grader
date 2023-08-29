vocals = ['a','e','i','o','u']

def jerigonzo(string):
    phrase = ''
    for l in string:
        if l in vocals:
            phrase = phrase + l + 'p' + l
        else:
            phrase = phrase + l
    return phrase