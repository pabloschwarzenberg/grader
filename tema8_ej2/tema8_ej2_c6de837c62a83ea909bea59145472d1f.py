def buscarTodas(a, b):
    z = 0
    a = list(a)
    indices = []
    final = ''
    while z < len(a):
        if b == a[z]:
            indices.append(z)
            indices.append(' ')
            z += 1
        else:
            z += 1

    indices.pop()
    for x in indices:
        final += str(x)



    return final
    
      

if __name__ == "__main__":
    pass