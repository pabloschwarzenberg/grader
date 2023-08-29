def es_primo(caca):
    d=2
    if caca==1:
      return False
    while d<caca:
        if (caca%d==0) or (caca==1):
            return False
            break
        d=d+1
    return True
            