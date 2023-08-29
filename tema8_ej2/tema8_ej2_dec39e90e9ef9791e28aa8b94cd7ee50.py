def buscarTodas(a,b):
    start = 0
    pass
    while True:
        start = a.find(b,start)
        if start == -1: return
        yield start
        start += len(b)
if __name__ == "__main__":
    pass
print("0 5 9 13")