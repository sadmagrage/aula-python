s = 0
n = int(input("Digite um número positivo: "))
if n>0:
    for x in range(1,n+1):
        s+=1/x
    print(s)
else:
    print("Número inválido.")