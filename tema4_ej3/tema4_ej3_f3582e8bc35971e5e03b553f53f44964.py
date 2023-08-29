def jerigonzo(string):
  
    if string.count("a")>=1:
       string=string.replace("a", "apa")
    if string.count("e")>=1:
       string=string.replace("e", "epe")
    if string.count("i")>=1:
       string=string.replace("i", "ipi")
    if string.count("o")>=1:
       string=string.replace("o", "opo")
    if string.count("u")>=1:
       string=string.replace("u", "upu")
    return string

if __name__ == "__main__":
    pass
         