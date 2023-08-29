sec = input()
adn = sec
adn.lower()

a = adn.count('a')
c = adn.count('c')
t = adn.count('t')
g = adn.count('g')

if (a+c+t+g == len(adn)):
  print('La {} actgacac es correcta'.format(sec))
  
else:
  print('La {} actgacac es incorrecta'.format(sec))