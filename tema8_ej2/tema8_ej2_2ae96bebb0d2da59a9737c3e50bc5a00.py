def buscarTodas(a,b):
    i = 0
    while i<=len(a):
      if a[i:i+len(b)] == b:
        return i
      i+=1

if __name__ == "__main__":
    a = input("Ingrese una palabra:")
    b = input("Ingrese una letra:")
    print(buscarTodas(a,b))