from time import  sleep
print("Olá aluno!")
nome = str(input("Por favor, digite seu nome completo: ")).strip().upper().split()
print("Bom dia Srº(a) {} {}".format(nome[0], nome[len(nome) - 1]))
sleep(1)
print("Seja bem vindo !!!")
sleep(2)
n1 = float(input("{} digite sua primeira nota: ".format(nome[0])))
n2 = float(input("{} digite sua segunda nota: ".format(nome[0])))
m = (n1 + n2) / 2
print("CALCULANDO...")
sleep(2)
if m >= 7.0:
     print("tirando {} e {} Sua média foi {}, e está ótima ! ".format(n1, n2, m))
     sleep(1)
     print("#PARABÈNS {},APROVADO".format(nome[0]))
elif m >= 5.0 and m < 7.0:
     print("tirando {} e {} Sua média foi {}, esperavamos mais! ".format(n1, n2, m))
     sleep(1)
     print("#FOI POR POUCO {}, VOCÊ VAI FICAR EM RECUPERAÇÃO".format(nome[0]))
else:
    print("tirando {} e {} Sua média foi {}, muito baixa! ".format(n1, n2, m))
    sleep(1)
    print("#NÃO FOI DESSA VEZ {}, VOCÊ ESTÁ REPROVADO".format(nome[0]))