turno = input("Digite o turno: ")
qntd = int(input("Digite o número de horas trabalhadas: "))
if turno=="a" or turno=="A":
    print("O salário é de R$%.2f"%37.5*qntd)
elif turno=="n" or turno=="N":
    print("O salário é de R$%.2f"%45*qntd)
else:
    print("O turno selecionado é inexistente.")