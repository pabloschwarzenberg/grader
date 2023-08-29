n = input()
n = int(n)

def prime_factors(n):
  if n == 1: return []
  for div in range(2, n + 1):
      if n % div == 0: return [div] + prime_factors(n // div)

print(prime_factors(n))