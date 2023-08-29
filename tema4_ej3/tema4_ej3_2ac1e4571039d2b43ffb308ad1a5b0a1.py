def jerigonzo(string):
  patpot = []
  for word in string:
    for pelu in word:
      if pelu in "aeiouAEIOU":
        pelu = pelu + "p" + pelu
      patpot.append(pelu)
  patpot = "".join(patpot)
  return patpot