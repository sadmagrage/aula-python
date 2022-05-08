idade = []
salario = []
while True:
    print("\033c")
    try:
        setIdade = str(input("Digite a idade, ou digite N para digitar o próximo dado Obs: O quantidade de idades inseridas deve ser a mesma quantidade de salários inseridos.\n"))
        if setIdade == "n" or setIdade == "N":
            break
        elif int(setIdade) < 0:
            break
        idade.append(setIdade)
    except:
        break
while True:
    print("\033c")
    try:
        if setIdade == "n" or setIdade == "N":
            setSalario = str(input("Digite o salário respectivo de cada idade em ordem, ou digite N para seguir:\n"))
            if setSalario == "n" or setSalario == "N":
                break
            salario.append(setSalario)
        elif int(setIdade) < 0:
            break
    except:
        break
try:
    if setIdade == "n" or setIdade == "N" and setSalario == "n" or setSalario == "N":
        print("\033c")
        if len(idade)>0:
            idade = list(map(int,idade))
            salario = list(map(float,salario))
            medIdade = 0
            for x in range(len(idade)):
                medIdade += idade[x]
            medIdade /= len(idade)
            print("A idade média é de {} anos.".format(medIdade))
        if len(salario)>0:
            idadeSuperior40 = []
            salarioSuperior40 = []
            for y in range(len(idade)):
                if idade[y]>40:
                    idadeSuperior40.append(idade[y])
                    salarioSuperior40.append(salario[y])
            medSalarioSuperior40 = 0
            for i in range(len(salarioSuperior40)):
                medSalarioSuperior40 += salarioSuperior40[i]
            if len(salarioSuperior40)>0:
                medSalarioSuperior40 /= len(salarioSuperior40)
            countLessThan600 = 0
            for c in range(len(salario)):
                if salario[c]<600:
                    countLessThan600+=1
            if len(idade) == len(salario):
                print("A média salarial dos indivíduos com mais de 40 anos é de R${:.2f} .\n{} indivíduos tem o salário menor que R$600,00.".format(medSalarioSuperior40,countLessThan600))
            else:
                print("O programa não contém o mesmo número de valores em idade e salário.")
except:
    print("Um dos valores inseridos não é valido.")