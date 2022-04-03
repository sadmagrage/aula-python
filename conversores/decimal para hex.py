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