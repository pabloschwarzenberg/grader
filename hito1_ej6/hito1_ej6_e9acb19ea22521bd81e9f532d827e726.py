#Ordenar tres números
a = eval(input('ingrese primer dato: '))
b = eval(input('ingrese segundo dato: '))
c = eval(input('ingrese tercer dato: '))

if a <= b <= c:
    print('el orden es:'  , (a, b, c))

if a <= c <= b:
    print('el orden es:'  , (a, c, b))

if b <= a <= c:
    print('el orden es:'  , (b, a, c))
          
if b <= c <= b:          
    print('el orden es:'  , (b, c, b))

if c <= a <= b:
    print('el orden es:'  , (c, a, b))

if c <= b <= a:
    print('el orden es:'  , (c, b, a))
