def hola(a,b):
    def sd(x):
      c=1
      u=0
      while (c<=x):
        if x%c==0:
            f=u+c
            u=f
        c=c+1
      return f
    if sd(a)==b or sd(b)==a:
      return("True")
    else:
      return("False")