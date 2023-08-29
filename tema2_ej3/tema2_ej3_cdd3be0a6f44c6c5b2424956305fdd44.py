def numero_perfecto(a):
    divs = 0
    var = True
    for n in range(1,a):
        if a%n == 0:
            divs += n
        if divs == a:
            var = True
        else:
            var = False
    return var