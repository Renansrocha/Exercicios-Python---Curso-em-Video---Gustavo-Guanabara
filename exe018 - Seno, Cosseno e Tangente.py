import math
ang= float(input("Digite o angulo que voce deseja: "))
seno= math.sin(math.radians(ang))
coseno= math.cos(math.radians(ang))
tangente= math.tan(math.radians(ang))
print("O Angulo de {} tem o Seno de {:.2f}".format(ang,seno))
print("O Angulo de {} tem o Cosseno de {:.2f}".format(ang,coseno))
print("O Angulo de {} tem a Tangente de {:.2f}".format(ang,tangente))

