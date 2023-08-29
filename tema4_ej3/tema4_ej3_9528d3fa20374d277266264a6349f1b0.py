string = 'estamos programando'
def jerigonzo(string):
    v = ['a','e','i','o','u']
    vv = []
    for i in string:
        vv.append(i)
        if i in v:
            vv.append('p')  
            vv.append(i)
    vvv = ''.join(vv)
    return vvv

print(jerigonzo(string))