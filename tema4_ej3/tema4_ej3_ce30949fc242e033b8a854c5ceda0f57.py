def jerigonzo(lucho):
    h=''
    for i in lucho:
        h+=i
        if i.lower() in ['a','e','i','o','u']:
            h+='p'
            h+=i
    return h
