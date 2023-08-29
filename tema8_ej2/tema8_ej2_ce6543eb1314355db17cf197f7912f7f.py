def buscarTodas(a,b):
      pos = ""    
      for i in range(len(a)):
           if b==a[i]:
               pos = pos + str(i) + " "
      pos = pos.rstrip(" ")
      return pos

if __name__ == "__main__":
    pass
               