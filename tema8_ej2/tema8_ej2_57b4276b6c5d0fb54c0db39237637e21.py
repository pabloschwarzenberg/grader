def buscarTodas(a,b):
    lookup = []
    for i in range(len(a)):
      temp = a[i:i+len(b)]
      if temp == b:
        lookup.append(i)
    return " ".join(map(str, lookup))

if __name__ == "__main__":
    pass
           