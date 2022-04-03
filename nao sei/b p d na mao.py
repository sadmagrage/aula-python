num = int(input("digite o numero binário de 10 dígitos: "))
x= 10
y= 2
dig1= num//x**9
dig2= num%x**9//x**8
dig3= num%x**8//x**7
dig4= num%x**7//x**6
dig5= num%x**6//x**5
dig6= num%x**5//x**4
dig7= num%x**4//x**3
dig8= num%x**3//x**2
dig9= num%x**2//x**1
dig10= num%x**1
d102p10= dig10*y**0
d92p10= dig9*y**1
d82p10= dig8*y**2
d72p10= dig7*y**3
d62p10= dig6*y**4
d52p10= dig5*y**5
d42p10= dig4*y**6
d32p10= dig3*y**7
d22p10= dig2*y**8
d12p10= dig1*y**9
d2p10= +d102p10+d92p10+d82p10+d72p10+d62p10+d52p10+d42p10+d32p10+d22p10+d12p10
print(dig1,dig2,dig3,dig4,dig5,dig6,dig7,dig8,dig9,dig10)
print(d2p10)
