def amigos(a,b):
    _diva = 0
    _divb = 0
    for divisor in range(1,a+1):
        if (a % divisor) == 0 :
            if(divisor != a):
                _diva = _diva + divisor
            
    for divisorb in range(1,b+1):
        if (b % divisorb) == 0 :
            if(divisorb != b):
                _divb = _divb + divisorb
          
    if(_diva == b and _divb == a):
        return True
        
    return False

resultado = amigos(220,284)
print(resultado)