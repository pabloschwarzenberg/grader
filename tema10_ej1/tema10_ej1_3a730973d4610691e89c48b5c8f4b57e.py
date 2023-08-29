def mcm(a,b,ab):
    if b == 0:
       numero = ab / a
       return numero
    else:
      ab = a * b
      sobra = a % b
      return mcm(b,sobra,ab)

if __name__=="__main__":
    pass
           