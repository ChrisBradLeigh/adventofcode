def calcFuel(mass):
    if (round(mass/3) > (mass/3)):
        return((round(mass/3)-1)-2)
    else:
        return((round(mass/3))-2)

def totalFuel(mass):
    total = 0
    while(mass > 0):
      if(calcFuel(mass) > 0):
        total += calcFuel(mass)
        mass = calcFuel(mass)
#        print("Total: " + str(total) + "   Mass: " + str(mass))
      else:
        break
    return total

file = open("modules.txt", "r")
total = 0
for modules in file:
    total += totalFuel(int(modules))
print(total)
