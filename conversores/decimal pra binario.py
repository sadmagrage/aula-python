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