def dpb():
    numero = int((input("Qual o número ? ")))
    aa=""
    while numero>0:
        resto=numero%2
        numero=numero//2
        aa+=str(resto)
    else:
        bb=len(aa)-1
        dd=""
        while bb>=0:
            cc=(aa[bb])
            dd+=str(cc)
            bb-=1
        else:
            print(dd)
def dpo():
    numero = int((input("Qual o número ? ")))
    aa=""
    while numero>0:
        resto=numero%8
        numero=numero//8
        aa+=str(resto)
    else:
        bb=len(aa)-1
        dd=""
        while bb>=0:
            cc=(aa[bb])
            dd+=str(cc)
            bb-=1
        else:
            print(dd)
def dph():
    numero = int((input("Qual o número ? ")))
    aa=""
    while numero>0:
        str(numero)
        resto=numero%16
        if resto==10:
            resto="A"
        elif resto==11:
            resto="B"
        elif resto==12:
            resto="C"
        elif resto==13:
            resto="D"
        elif resto==14:
            resto="E"
        elif resto==15:
            resto="F"
        numero=numero//16
        aa+=str(resto)
    else:
        bb=len(aa)-1
        dd=""
        while bb>=0:
            cc=(aa[bb])
            dd+=str(cc)
            bb-=1
        else:
            print(dd)
x="1"
while x=="1":
    conversao=input("Qual opção deseja converter, digite 1 para binário, 2 para octal, 3 para hexadecimal ou 0 para sair. ")
    if conversao=="1":
        dpb()
        x+="1"
    elif conversao=="2":
        dpo()
        x+="1"
    elif conversao=="3":
        dph()
        x+="1"
    elif conversao=="0":
        break
    else:
        print("A opção selecionada é inexistente.")
    x=input("Para realizar outra operação, digite 1. ")