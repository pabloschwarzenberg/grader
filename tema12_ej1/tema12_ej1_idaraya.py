def binario(num):
    exp=num
    result=''
    while num > 1:
	    d=num%2
	    result+=str(d)
	    num=num//2
    

    result+='1'
    result=list(result)
    result.reverse()
    result=''.join(result)
    return result


n=int(input('ingrese largo del numero binario: '))

max=(2**(n))-1
while max>1:
    binarios=binario(max)
    while len(binarios)<n:
              binarios='0'+binarios
    print(binarios)
    max-=1
    
print(('0'*(n-1))+'1')
print('0'*n)