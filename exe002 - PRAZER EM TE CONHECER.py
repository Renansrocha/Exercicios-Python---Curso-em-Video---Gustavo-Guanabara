
nome = str(input('Digite seu nome: '))
print('È um prazer te conhecer {:=^20}'.format(nome))
#Com cores
nome = str(input('Digite seu nome: '))
cores = {"limpa":"\033[m",
             'azul':"\033[34m",
             'amarelo':"\033[33m",
             'pretoebranco':"\033[30;107m"}
print('È um prazer te conhecer {}{:=^20}{}'.format(cores['amarelo'], nome, cores["limpa"]))
