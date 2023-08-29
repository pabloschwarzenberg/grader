def jerigonzo(string):
    s=""
    for i in range(len(string)):
      if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
         s=s+string[i]+"p"+string[i]
      else:
         s=s+string[i]
    return s

if __name__ == "__main__":
    pass
         