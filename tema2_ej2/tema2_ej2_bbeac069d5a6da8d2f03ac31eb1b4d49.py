def num_amigos(a,b):
    divA = divisores(a)
    divB = divisores(b)
    if sum(divA) == b:
        return print("Son numeros amigos")
    elif sum(divB) == a:
        return print("Son numeros amigos")
    else:
        return print("No son numeros amigos")
        
 def divisores(n):
    div = []
    i = 1
    while n >= i:
        if n % i == 0:
            div.append(i)
            i += 1
        else:
            i += 1
    return div