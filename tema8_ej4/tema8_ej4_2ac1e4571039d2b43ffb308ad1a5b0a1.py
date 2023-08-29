def rot13(w):
    pop = "abcdefghijklmnopqrstuvwxyz"
    jell = pop[13:] + pop[:13]
    rot_pop = lambda x: jell[pop.find(x)] if pop.find(x) > -1 else x
    return ''.join(rot_pop(x) for x in w)