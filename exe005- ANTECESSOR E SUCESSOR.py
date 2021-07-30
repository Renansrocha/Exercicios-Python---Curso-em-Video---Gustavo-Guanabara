n = int(input ('Digite um número: '))
print('Analisando o valor {}, seu antecesor é {}, e o sucessor é {}'.format(n, n-1, n+1))

#Com cores
n = int(input('Digite um número: '))
print("Analisando o valor ""\033[31m""{}""\033[m"", seu antecesor é ""\033[31m""{}""\033[m"", e o sucessor é ""\033[31m""{}""\033[m""".format(n, n-1, n+1))
