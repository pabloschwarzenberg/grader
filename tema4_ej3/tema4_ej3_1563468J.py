def jerigonzo(p):
    copia=""
    for n in p:
        if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
            n=n+"p"+n
        copia+=n

    return copia
    
if __name__ == "__main__":
    pass
