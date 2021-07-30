


print("-=-" * 10)
print("   Analisador de triângulos")
print("-=-" * 10)
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo", end=" ")
    if r1 == r2 == r3:
        print("EQUILATÉRO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÒSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")






'''print("-=-" * 10)
print("   Analisador de triângulos")
print("-=-" * 10)
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))
if r1 != r2 and r1 != r3 and r2 != r3:
    print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")
elif r1 == r2 and r1 and r2 != r3 or r2 == r3 and r2 and r3 != r1 or r3 == r1 and r3 and r1 != r2:
    print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES")
elif r1 == r2 and r3 or r2 == r3 and r1 or r3 == r2 and r1:
    print("Os segmentos acima PODEM FORMAR um triângulo EQUILATÉRO")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")'''
