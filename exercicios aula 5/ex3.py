valor=float(input("Digite o valor da compra: "))
if valor>200:
    print("O valor da compra com desconto foi de %.2f"%(valor*0.8))
else:
    print("O valor da compra foi de %.2f"%(valor*1.0))