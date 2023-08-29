def suma_divisores (n):
	divisores = [ i for i in range(1,n + 1) if n % i == 0]

	return sum(divisores)


  a1 = int(input('digito 1: '))
  b2 = int(input('digito 2: '))
  a = suma_divisores(a1)
  b = suma_divisores(b2)

def amigos(a,b):
    if a == b:
        return true
    else:
        return false           