from math import hypot
co= float(input("Qual o comprimento do cateto oposto: "))
ca= float(input("Qual o comprimento do cateto adjacente: "))
hi = hypot(co,ca)
print("A hipotenusa vai medir {:.2f}".format(hi))


# co= float(input("Qual o comprimento do cateto oposto: "))
# ca= float(input("Qual o comprimento do cateto adjacente: "))
# hi= (co**2+ ca**2)** (1/2)
# print("A hipotenusa vai medir {:.2f}".format(hi))