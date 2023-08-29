def buscarTodas(a,b):
    A = 0
    B = False
    
    while A < len(a) and not B:
        if a[A] == b:
            B = True
        else:
            A += 1
    return A

if __name__ == "__main__":
    pass
           