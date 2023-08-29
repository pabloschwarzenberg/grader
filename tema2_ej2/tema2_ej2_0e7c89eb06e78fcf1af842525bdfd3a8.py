def amigos(a,b):
    divisores = [ d for d in range(1,a//2+1) if a % d == 0 ]
    if sum(divisores) == b:
        divisores = [ d for d in range(1,b//2+1) if b % d == 0 ]
        if sum(divisores) == a:
            return True
  
  
    return False