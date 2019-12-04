def main():
  min = 171309
  max = 643603

  count1 = 0
  count2 = 0
  for x in range (min, max):
    if checkPassword1(x):
      count1 += 1
    if checkPassword2(x):
      count2 += 1
  print(count1)
  print(count2)

def checkPassword1(password):
  isValid = False
  password = str(password)
  for x in range(0, len(password)-1):
    if password[x+1] < password[x]:
      return False
    if password[x] == password[x+1]:
      isValid = True
  return isValid

def checkPassword2(password):
  isValid = False
  password = str(password)
  for x in range(0, len(password)-1):
    if password[x+1] < password[x]:
      return False
    if password[x] == password[x+1] and password.count(password[x]) == 2:
      isValid = True
  return isValid

if __name__ == "__main__":
    main()
