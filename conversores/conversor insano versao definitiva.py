def dpd():
    mesmonum=int(input("Qual o número ? "))
    print(mesmonum)
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
def bpb():
    num = input("Qual o número ? ")
    i=0
    aa=0
    bb=len(num)-1
    while i<len(num):
        if num[i] == "0" or num[i] == "1":
            numa=int(num[i])
            bb-=1
            i+=1
        else:
            print("O número digitado é inválido")
            break
    else:
        print(num)
def bpo():
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
            print("o número digitado é inválido")
            break
    else:
        numero=aa
        ee=""
        while numero>0:
            resto=numero%8
            numero=numero//8
            ee+=str(resto)
        else:
            bb=len(ee)-1
            dd=""
            while bb>=0:
                cc=(ee[bb])
                dd+=str(cc)
                bb-=1
            else:
                print(dd)
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
            print("o número digitado é inválido")
            break
    else:
        print(aa)
def bph():
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
            print("o número digitado é inválido")
            break
    else:
        ee=""
        while aa>0:
            str(aa)
            resto=aa%16
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
            aa=aa//16
            ee+=str(resto)
        else:
            bb=len(ee)-1
            dd=""
            while bb>=0:
                cc=(ee[bb])
                dd+=str(cc)
                bb-=1
            else:
                print(dd)
def opb():
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
        ee=""
        while aa>0:
            resto=aa%2
            aa=aa//2
            ee+=str(resto)
        else:
            bb=len(ee)-1
            dd=""
            while bb>=0:
                cc=(ee[bb])
                dd+=str(cc)
                bb-=1
            else:
                print(dd)
def opo():
    mesmonum=int(input("Qual o número ? "))
    print(mesmonum)
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
def oph():
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
        ee=""
        while aa>0:
            str(aa)
            resto=aa%16
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
            aa=aa//16
            ee+=str(resto)
        else:
            bb=len(ee)-1
            dd=""
            while bb>=0:
                cc=(ee[bb])
                dd+=str(cc)
                bb-=1
            else:
                print(dd)
def hpb():
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
                print("Carácter inválido")
                break
            numa=int(cc)*16**bb
        aa+=numa
        bb-=1
        i+=1
    else:
        ee=""
        while aa>0:
            resto=aa%2
            aa=aa//2
            ee+=str(resto)
        else:
            bb=len(ee)-1
            dd=""
            while bb>=0:
                cc=(ee[bb])
                dd+=str(cc)
                bb-=1
            else:
                print(dd)
def hpo():
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
                print("Carácter inválido")
                break
            numa=int(cc)*16**bb
        aa+=numa
        bb-=1
        i+=1
    else:
        ee=""
        while aa>0:
            resto=aa%8
            aa=aa//8
            ee+=str(resto)
        else:
            bb=len(ee)-1
            dd=""
            while bb>=0:
                cc=(ee[bb])
                dd+=str(cc)
                bb-=1
            else:
                print(dd)
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
                print("Carácter inválido")
                break
            numa=int(cc)*16**bb
        aa+=numa
        bb-=1
        i+=1
    else:
        print(aa)
def hph():
    num = input("Qual o número ? ")
    i=0
    while i<len(num):
        if num[i]!="0" and num[i]!="1" and num[i]!="2" and num[i]!="3" and num[i]!="4" and num[i]!="5" and num[i]!="6" and num[i]!="7" and num[i]!="8" and num[i]!="9" and num[i]!="A" and num[i]!="a" and num[i]!="B" and num[i]!="b" and num[i]!="C" and num[i]!="c" and num[i]!="D" and num[i]!="d" and num[i]!="E" and num[i]!="e" and num[i]!="F" and num[i]!="f":
            print("Carácter inválido")
            break
        i+=1
    else:
        print(num)
reinicio="1"
while reinicio=="1":
    conversaoi=int(input("Digite 10 para converter um número decimal, 2 para converter um número binário, 8 para converter um número octaldecimal, 16 para converter um número hexadecimal: "))
    conversaof=int(input("Digite 10 para converter para um número decimal, 2 para converter para um número binário, 8 para converter para um número octaldecimal, 16 para converter para um número hexadecimal: "))
    if conversaoi==10 and conversaof==10:
        dpd()
    elif conversaoi==10 and conversaof==2:
        dpb()
    elif conversaoi==10 and conversaof==8:
        dpo()
    elif conversaoi==10 and conversaof==16:
        dph()
    elif conversaoi==2 and conversaof==2:
        bpb()
    elif conversaoi==2 and conversaof==8:
        bpo()
    elif conversaoi==2 and conversaof==10:
        bpd()
    elif conversaoi==2 and conversaof==16:
        bph()
    elif conversaoi==8 and conversaof==2:
        opb()
    elif conversaoi==8 and conversaof==8:
        opo()
    elif conversaoi==8 and conversaof==10:
        opd()
    elif conversaoi==8 and conversaof==16:
        oph()
    elif conversaoi==16 and conversaof==2:
        hpb()
    elif conversaoi==16 and conversaof==8:
        hpo()
    elif conversaoi==16 and conversaof==10:
        hpd()
    elif conversaoi==16 and conversaof==16:
        hph()
    else:
        print("As opções de conversão selecionadas estão incorretas.")
    reinicio=input("Se desejar realizar outra operação digite 1, caso contrário, digite qualquer outra coisa. ")