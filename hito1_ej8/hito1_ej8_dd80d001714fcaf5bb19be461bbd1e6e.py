n = input('numero: ')
l = len(n)
i = 0
r = ''
b = 'UDCM'
while i < l:
    r = r+n[i]+b[l-1-i]+'+'
    i += 1
print(r[:-1])