
vocals = ['a','e','i','o','u']

def jerigonzo(string):
    phrase = ''
    for k in string:
        if k in vocals:
            phrase = phrase + k + 'p' + k
        else:
            phrase = phrase + k
    return phrase
