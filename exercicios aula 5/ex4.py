agua=int(input("Digite o valor da conta de água: "))
luz=int(input("Digite o valor da conta de luz: "))
telefone=int(input("Digite o valor da conta de telefone: "))
salario=int(input("Digite o salário: "))
total=salario-(agua+luz+telefone)
if total>=0:
    print("O salário é de R$%.2f"%total)
else:
    print("Salário insuficiente.")