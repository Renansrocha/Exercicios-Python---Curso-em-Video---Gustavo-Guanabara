from random import randint
computador = randint(0, 10)  # Faz o computador pensar
nome = str(input("Digite seu nome jogador: ")).strip().upper()
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Vou pensar em um número \033[4;34m{}\033[m, entre 0 e 10. Tente adivinhar...".format(nome))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite:  "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("mais... Tente novamente: ")
        elif jogador > computador:
            print("menos... Tente novamente: ")
print("Acertou com {} tentativas. Parabéns.".format(palpite))

