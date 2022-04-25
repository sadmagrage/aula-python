peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/altura**2

print('IMC = %.2f' %(imc))

if imc < 20:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso normal')
elif imc <= 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obeso')
else:
    print('Obeso mórbido')