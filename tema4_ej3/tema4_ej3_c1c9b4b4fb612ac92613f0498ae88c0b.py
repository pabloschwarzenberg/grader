def jerigonzo(string):
  efe = lambda s: ''.join([a+'p'+a if a in 'aeiou' else a for a in s.lower()])
  string=efe(string)
  return string