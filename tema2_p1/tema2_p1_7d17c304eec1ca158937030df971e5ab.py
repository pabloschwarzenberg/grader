def es_primo(n):
	if n<=1:
		return False
	elif n==2:
		return True
	elif n % 2 == 0:
		return False

	factor = 3
	while factor * factor <= n:
		if n % factor == 0:
			return False
		factor+=2

	return True

n=int(10)

print('')
print(es_primo(n))
           