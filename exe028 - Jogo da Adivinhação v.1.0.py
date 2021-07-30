from random import randint
from time import sleep
nome = str(input("Digite seu nome jogador: ")).strip().upper()
sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Vou pensar em um número {}, entre 0 e 5. Tente adivinhar...".format(nome))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
sleep(3)
jogador = int(input("Em que numero pensei? ")) #Jogador tenta adivinhar
computador = randint(0, 5) #Faz o computador pensar
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("Parabéns {}, você  acertou e me venceu, realmente pensei no número {}!!!".format(nome, computador))
else:
    print("Ganhei de voce {}, pensei no número {} e não no número {}".format(nome, computador, jogador))

