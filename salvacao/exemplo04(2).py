#Exemplo 04 - Condicional Composto

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você pode ter CNH")
else:
    print("Você não pode ter CNH")
    tempo = 18 - idade
    print("Faltam:", tempo, "anos")

print("Palmeiras não tem mundial")
