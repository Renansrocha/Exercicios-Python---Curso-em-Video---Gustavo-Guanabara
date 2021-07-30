from time import sleep

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite mais um valor: "))
opção = 0
while opção != 5:
    print("Escolha uma opção! ")
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA ''')
    opção = int(input("Qual opção:"))
    if opção == 1:
        print(" A soma de {:.0f} + {:.0f} é = {:.0f}.".format(n1, n2, (n1 + n2)))
    elif opção == 2:
        print(" A multiplicação de {:.0f} x {:.0f} é = {:.0f}.".format(n1, n2, (n1 * n2)))
    elif opção == 3:
        if n1 > n2:
            print("O maior número entre {:.0f} e {:.0f}, o maior é o {:.0f}.".format(n1, n2, n1))
        if n2 > n1:
            print("O maior número entre {:.0f} e {:.0f}, o maior é o  {:.0f}.".format(n1, n2, n2))
        if n1 == n2:
            print("Você digitou os números iguais ! ")
    elif opção == 4:
        print("Informe os números novamente: ")
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite mais um valor: "))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Você digitou uma opçãp invalida. Tente novamente: ")
    print("=-="*10)
    sleep(2)
print("Fim do programa. Volte sempre!")

# Opção Usando if e elif
'''n1 = float(input("Digite um valor: "))
n2 = float(input("Digite mais um valor: "))
print("Escolha uma opção! ")
print("[ 1 ] SOMA ")
print("[ 2 ] MULTIPLICAR ")
print("[ 3 ] MAIOR ")
print("[ 4 ] NOVOS NÚMEROS ")
print("[ 5 ] SAIR DO PROGRAMA ")
opção = int(input("Qual opção: "))
if opção == 1:
    print(" A soma de {:.0f} + {:.0f} é = {:.0f}.".format(n1, n2, (n1 + n2)))
elif opção == 2:
    print(" A multiplicação de {:.0f} x {:.0f} é = {:.0f}.".format(n1, n2, (n1 * n2)))
elif opção == 3:
    if n1 > n2:
        print("O maior número entre {:.0f} e {:.0f}, o maior é o {:.0f}.".format(n1, n2, n1))
    if n2 > n1:
        print("O maior número entre {:.0f} e {:.0f}, o maior é o  {:.0f}.".format(n1, n2, n2))
    if n1 == n2:
        print("Você digitou os números iguais ! ")
elif opção == 5:
    print("Ok, você escolheu sair...")
while opção == 4:
    n1 = float(input("Digite um valor: "))
    n2 = float(input("Digite mais um valor: "))
    print("Escolha uma opção! ")
    print("[ 1 ] SOMA ")
    print("[ 2 ] MULTIPLICAR ")
    print("[ 3 ] MAIOR ")
    print("[ 4 ] NOVOS NÚMEROS ")
    print("[ 5 ] SAIR DO PROGRAMA ")
    opção = int(input("Qual opção: "))
    if opção == 1:
        print(" A soma de {:.0f} + {:.0f} é = {:.0f}.".format(n1, n2, (n1 + n2)))
    elif opção == 2:
        print(" A multiplicação de {:.0f} x {:.0f} é = {:.0f}.".format(n1, n2, (n1 * n2)))
    elif opção == 3:
        if n1 > n2:
            print("O maior número entre {:.0f} e {:.0f}, o maior é o {:.0f}.".format(n1, n2, n1))
        if n2 > n1:
            print("O maior número entre {:.0f} e {:.0f}, o maior é o  {:.0f}.".format(n1, n2, n2))
        if n1 == n2:
            print("Você digitou os números iguais ! ")
    elif opção == 5:
        print("Ok, você escolheu sair...")'''
