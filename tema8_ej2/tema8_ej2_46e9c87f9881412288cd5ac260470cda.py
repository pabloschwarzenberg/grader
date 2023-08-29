def buscarTodas(a,b):
    i = 0
    j = 0
    while i < len(a):
        if b == a[i]:
            j = j + 1
        i = i + 1 
    return j
print(buscarTodas('tres tristes tigres','t'))
    pass

if __name__ == "__main__":
    pass
           