conversaoi=int(input("Digite 10 para converter um número decimal, 2 para converter um número binário, 8 para converter um número octaldecimal, 16 para converter um número hexadecimal: "))
conversaof=int(input("Digite 10 para converter para um número decimal, 2 para converter para um número binário, 8 para converter para um número octaldecimal, 16 para converter para um número hexadecimal: "))
if conversaoi==10 and conversaof==10:
    mesmonum=int(input("Qual o número ? "))
    print(mesmonum)
elif conversaoi==10 and conversaof==2:
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
elif conversaoi==10 and conversaof==8:
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
elif conversaoi==10 and conversaof==16:
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
elif conversaoi==2 and conversaof==2:
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
elif conversaoi==2 and conversaof==8:
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
elif conversaoi==2 and conversaof==10:
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
elif conversaoi==2 and conversaof==16:
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
elif conversaoi==8 and conversaof==2:
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
elif conversaoi==8 and conversaof==8:
    mesmonum=int(input("Qual o número ? "))
    print(mesmonum)
elif conversaoi==8 and conversaof==10:
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
elif conversaoi==8 and conversaof==16:
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
elif conversaoi==16 and conversaof==2:
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
                print("caracter invalido")
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
elif conversaoi==16 and conversaof==8:
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
                print("caracter invalido")
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
elif conversaoi==16 and conversaof==10:
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
                print("caracter invalido")
                break
            numa=int(cc)*16**bb
        aa+=numa
        bb-=1
        i+=1
    else:
        print(aa)
elif conversaoi==16 and conversaof==16:
    mesmonum=int(input("Qual o número ? "))
    print(mesmonum)