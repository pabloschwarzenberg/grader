# completa el código de la función
def amigos(a, b):
    div_a = []
    div_b = []
    for i in range(a//2):
        if a//(i+1) == a/(i+1):
            div_a.append(i+1)
    for i in range(b//2):
        if b//(i+1) == b/(i+1):
            div_b.append(i+1)
    if sum(div_a) == b and sum(div_b) == a:
        return True
    return False