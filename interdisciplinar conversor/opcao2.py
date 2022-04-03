def bpd():
    num = input("Qual o número ? ")
    i=0
    aa=0
    bb=len(num)-1
    while i<len(num):
        if num[i] == "0" or num[i] == "1":
            numa=int(num[i])*2**bb
            bb-=1
            aa+=numa
            i+=1
        else:
            print("O número digitado é invalido.")
            break
    else:
        print(aa)
def opd():
    num = input("Qual o número ? ")
    i=0
    aa=0
    bb=len(num)-1
    while i<len(num):
        numa=int(num[i])*8**bb
        bb-=1
        aa+=numa
        i+=1
    else:
        print(aa)
def hpd():
    num = input("Qual o número ? ")
    i=0
    aa=0
    bb=len(num)-1
    while i<len(num):
        if num[i]=="0" or num[i]=="1" or num[i]=="2" or num[i]=="3" or num[i]=="4" or num[i]=="5" or num[i]=="6" or num[i]=="7" or num[i]=="8" or num[i]=="9":
            numa=int(num[i])*16**bb
        else:
            cc=num[i]
            if num[i]=="A" or num[i]=="a":
                cc=10
            elif num[i]=="B" or num[i]=="b":
                cc=11
            elif num[i]=="C" or num[i]=="c":
                cc=12
            elif num[i]=="D" or num[i]=="d":
                cc=13
            elif num[i]=="E" or num[i]=="e":
                cc=14
            elif num[i]=="F" or num[i]=="f":
                cc=15
            else:
                print("Carácter inválido.")
                break
            numa=int(cc)*16**bb
        aa+=numa
        bb-=1
        i+=1
    else:
        print(aa)
x="1"
while x=="1":
    conversao=input("Se deseja converter do binário, digite 1, 2 do octaldecimal, 3 hexadecimal ou 0 para finalizar. ")
    if conversao=="1":
        bpd()
        x+="1"
    elif conversao=="2":
        opd()
        x+="1"
    elif conversao=="3":
        hpd()
        x+="1"
    elif conversao=="0":
        break
    else:
        print("A opção é inexistente.")
    x=input("Digite 1 para realizar outra operação. ")