x=0
while x==0:
    horas = int(input("Digite o valor em horas: "))
    print("O valor em horas para minutos é de: ",horas*60)
    x=int(input("Tentar novamente ? Digite 0, para finaliza a operação, digite 1. "))
    print("\033c")