'''Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print("\033[1;97m="*30)
print("{:^30}".format("BANCO CEV"))
print("="*30)
valor = int(input("Qual valor você quer sacar? R$:"))
total = valor
cedula = 50
totaldecedula = 0
while True:
    if total >= cedula:  #Verifica o valor total se é o mamior ou igual que a cedula
        total -= cedula  #Verifica se dá pra tirar o valor das cedulas do total
        totaldecedula += 1  # Contador de cedulas retirada do total
    else:
        if totaldecedula > 0:  # O programa só ira escrever se o total de cedulas for maior que 0.
          print(f"Total de {totaldecedula} de cédulas de R${cedula}.")  #Print da quantidade de cedulas e o valor delas
        if cedula == 50:  #Se a cedula atual for igual 50, e não der pra tirar mais esse valor, segue abaixo.
            cedula = 20  # A proxima cedula vira 20.
        elif cedula == 20:  #Se a cedula atual for igual 20, e não der pra tirar mais esse valor, segue abaixo.
            cedula = 10   # A proxima cedula vira 10.
        elif cedula == 10:  #Se a cedula atual for igual10, e não der pra tirar mais esse valor, segue abaixo.
            cedula = 1  # A proxima cedula vira 1.
        totaldecedula = 0  #Contador de cedulas
        if total == 0:  #Quando o valor total atintig 0 o programa para.
            break
print("="*30)
print("Volte sempre ao BANCO CEV ! tenha um bom dia !")

