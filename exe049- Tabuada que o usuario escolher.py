nome = str(input("Digite seu nome completo: ")).upper().strip()
print("Seja bem vindo {} a ""\033[1;30;43mTABUADA ONLINE\033[m".format(nome))
n = int(input("Digite um número para saber sua tabuada: "))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
