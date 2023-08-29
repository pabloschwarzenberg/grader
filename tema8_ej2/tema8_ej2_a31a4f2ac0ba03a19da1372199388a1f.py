def buscarTodas(a, b):
    import re
    z = [m.start() for m in re.finditer(b,a)]
    w = " ".join(str(x) for x in z)
    p = w.strip()
    return p