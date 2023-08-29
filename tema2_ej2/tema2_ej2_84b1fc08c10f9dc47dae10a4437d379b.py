def amigos(a,b):
    if a == b:
      return False
    ama = []
    amb = []
    for i in range(1, a+1):
        if a%i == 0:
            ama.append(i)
    for i in range(1, b+1):
        if b%i == 0:
            amb.append(i)
    sa = sum(ama)
    sb = sum(amb)
    if sa == sb:
        return True
    return False