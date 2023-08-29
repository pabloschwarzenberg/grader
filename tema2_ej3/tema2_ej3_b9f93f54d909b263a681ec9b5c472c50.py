def numero_perfecto(h):
    sumatoria = 0

    for i in range(1, h):
        if h % i == 0:
            sumatoria += i

    return sumatoria == h