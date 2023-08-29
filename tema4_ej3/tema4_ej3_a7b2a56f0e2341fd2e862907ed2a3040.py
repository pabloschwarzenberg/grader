def jerigonzo(a):
  b=list(a) 
  for c in a:
      if c=="a":
        x=int(b.index("a"))
        b[x]=("apa")
      elif c=="e":
        x=int(b.index("e"))
        b[x]=("epe")
      elif c=="i":
        x=int(b.index("i"))
        b[x]=("ipi")
      elif c=="o":
        x=int(b.index("o"))
        b[x]=("opo")
      elif c=="u":
        x=int(b.index("u"))
        b[x]=("upu")
  return("".join(b))
    

if __name__ == "__main__":
    pass
         