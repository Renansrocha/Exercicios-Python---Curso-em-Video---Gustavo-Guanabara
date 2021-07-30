"""Exercício Python 68:
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
print("\033[1;41;97mVAMOS JOGAR PAR OU IMPAR?\033[m")
v = 0
while True:
    jogador = int(input("Digite seu número: "))  # Jogador
    cpu = randint(0, 10)  # Computador
    total = jogador + cpu  #Soma do jogador e computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou impar? [P/I] ")).upper().strip()[0]  # Variavel para indentificar par ou impar
    print(f"Você jogou {jogador} e o computador jogou {cpu}. Total de {total} ", end=" ")
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR ")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU")
            v += 1
        else:
            print("Você PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Voce VENCEU")
            v += 1
        else:
            print("Você PERDEU")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER ! Você venceu {v} vezes.")
