def jerigonzo(string):
    vocales = list('aeiouáéíóú')

    new_string = ''

    for l in string:
      if l.lower() in vocales:
        new_string += l + 'p' + l.lower()
      else:
        new_string += l

    return new_string

if __name__ == "__main__":
    print(jerigonzo(input()))
         
