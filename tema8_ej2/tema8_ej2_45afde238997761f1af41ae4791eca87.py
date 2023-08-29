def buscarTodas(a, b):
    indices = [str(i) for i in range(len(a)) if a[i:i+len(b)] == b]
    return ' '.join(indices)
           