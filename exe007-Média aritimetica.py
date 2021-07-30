# #Forma simples
'''nome = input('Olá aluno, digite seu nome: ')
print ('Bem vindo', nome)
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
print(nome, 'Sua media é: {}'.format((n1+n2)/2))'''


# #Forma melhorada
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
if m >= 6.0:
     print("Sua média foi {}, e está ótima ! ".format(m))
     sleep(1)
     print("#PARABÈNS {}".format(nome[0]))
else:
     print("Sua média  foi {} e está ruim !".format(m))
     sleep(1)
     print("#ESTUDE MAIS {}".format(nome[0]))