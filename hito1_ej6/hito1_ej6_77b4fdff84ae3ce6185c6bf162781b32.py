a= eval(input('ingrese un numero:'))
b= eval(input('ingrese un numero:'))
c= eval(input('ingrese un numero:'))

if a>=b>=c:
  print('el orden es:', c,",",b",",a)
if a>=c>=b:
  print('el orden es:', b,",",c,",",a)
if b>=a>=c:
  print('el orden es:', c,",",a,",",b)
if b>=c>=a:
  print('el orden es:', a,",",c,",",b)
if c>=a>=b:
  print('el orden es:', b,",",a,",",c)
if c>=b>=a:
  print('el orden es:', a,",",b,",",c)

  

