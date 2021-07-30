from time import sleep
from random import randint
print('{:^40}'.format('===============\033[4;34;33mBEM VINDO AO JOGO\033[m================'))
print('''Escolha:
{ 0 ]  PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Digite sua escolha? "))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print("=-=-=-=-=\033[97;41mJO\033[m-=-=-=-=-=-")
sleep(1)
print("=-=-=-=-=-=\033[97;41mKEN\033[m-=-=-=-=-=-=-")
sleep(1)
print("=-=-=-=-=-=-=-\033[97;41mPO\033[m-=-=-=-=-=-=-=-=")
sleep(1)
print("\033[30;107m/\033[m"*30)
print("O COMPUTADOR escolheu {}".format(itens[computador]))
print("O JOGADOR escolheu {}".format(itens[jogador]))
print("\033[107;30m/\033[m"*30)
if computador == 0:
    if jogador == 0:
        print("O jogo deu \033[1;97;41mEMPATE\033[m")
    elif jogador == 1:
        print("Você \033[1;97;41mGANHOU\033[m")
    elif jogador == 2:
        print("Você \033[1;97;41mPERDEU\033[m")
    else:
        print("JOGADA INVALIDA")
elif computador == 1:
    if jogador == 0:
        print("Você \033[1;97;41mPERDEU\033[m")
    elif jogador == 1:
        print("O jogo deu \033[1;97;41mEMPATE\033[m")
    elif jogador == 2:
        print("Você \033[1;97;41mGANHOU\033[m")
    else:
        print("JOGADA INVALIDA")
elif computador == 2:
    if jogador == 0:
        print("Você \033[1;97;41mGANHOU\033[m")
    elif jogador == 1:
        print("Você \033[1;97;41mPERDEU\033[m")
    elif jogador == 2:
        print("O jogo deu \033[1;97;41mEMPATE\033[m")
    else:
        print("JOGADA INVALIDA")







