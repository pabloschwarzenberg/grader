def numero_perfecto(a):
    divisores = [l for l in range(1,a) if a % l == 0]
    suma = sum(divisores)
    perf = False
    if suma == a:
        perf = True
    return perf
    


           