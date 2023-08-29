def buscarTodas(a,b):
    z = ""
    for i in range(len(a)):
        if a[i] == b:
            z = z + " " + str(i)
            z = z.strip()
    return z

if __name__ == "__main__":
    a = input()
    b = input()       
    print(buscarTodas(a,b))

    
           