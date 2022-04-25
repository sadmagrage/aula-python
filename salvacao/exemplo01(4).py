#exemplo 01 

m = float(input('Digite a sua média: '))
f = float(input('Digite a sua frequencia: '))

if f < 75:
    print('Reprovado por falta')
else: 
    if m < 6:
        print('Reprovado por nota')
    else:
        print('Aprovado')