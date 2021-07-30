n = int(input("Digite um número: "))
print('O dobro de', n, 'vale {}'.format(n * 2))
print('O triplo de', n, 'vale {}'.format(n * 3))
print('A Raiz quadrada de', n, 'vale {:.2F}'.format(n ** (1 / 2)))

#Com cores

n = int(input("Digite um número: "))
print("O ""\033[4;34m""dobro""\033[m" " de", n, "vale {}".format(n * 2))
print("O ""\033[4;34m""triplo""\033[m" " de", n, 'vale {}'.format(n * 3))
print("A ""\033[4;34m""raiz quadrada""\033[m", " de", n, 'vale {:.2F}'.format(n ** (1 / 2)))

