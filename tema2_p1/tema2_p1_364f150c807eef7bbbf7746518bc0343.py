def es_primo(num):
    a = num
    c = []
    if num == 1:
        x = 'False'
    else:
        while a != 0:
            c.append(num % a)
            a = a - 1
        pass
    if c.count(0) == 2:
        x = True
    else:
        x = False
    return(x)