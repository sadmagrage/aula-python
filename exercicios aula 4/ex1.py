import math
altura = float(input("digite o valor da altura: "))
baseM = float(input("digite o valor da base maior: "))
basem = float(input("digite o valor da base menor: "))
volume = altura/3*(math.pow(baseM,2)+math.pow(basem,2)+math.pow(math.pow(baseM,2)*math.pow(basem,2),0.5))
print(volume)