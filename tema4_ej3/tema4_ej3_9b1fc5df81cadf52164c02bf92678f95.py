def jerigonzo(string):
  string_l = list(string)
  i = 0
  j = 0
  k = 0
  while i<len(string_l):
    if string_l[i]=='a' and ((i<(len(string_l)-1) and string_l[i+1]!=')') or i==(len(string_l)-1)):
      string_l.insert((i+1),'(pa)')
      j += 1
    elif string_l[i]=='e' and ((i<(len(string_l)-1) and string_l[i+1]!=')') or i==(len(string_l)-1)):
      string_l.insert((i+1),'(pe)')
      j += 1
    elif string_l[i]=='i' and ((i<(len(string_l)-1) and string_l[i+1]!=')') or i==(len(string_l)-1)):
      string_l.insert((i+1),'(pi)')
      j += 1
    elif string_l[i]=='o' and ((i<(len(string_l)-1) and string_l[i+1]!=')') or i==(len(string_l)-1)):
      string_l.insert((i+1),'(po)')
      j += 1
    elif string_l[i]=='u' and ((i<(len(string_l)-1) and string_l[i+1]!=')') or i==(len(string_l)-1)):
      string_l.insert((i+1),'(pu)')
      j += 1
    i += 1
  string = ''.join(string_l)
  string_l = list(string)
  while k<j:
    string_l.remove('(')
    string_l.remove(')')
    k += 1
  string = ''.join(string_l)
  return string


if __name__ == "__main__":
  palabra = input('Ingresar palabra: ')
  print(jerigonzo(palabra))
         