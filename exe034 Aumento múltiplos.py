#forma simplificada
salario = float(input('Qual o salário do funcionário: R$'))
if salario >= 1250.0:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario:.2f}, com  novo aumento passa a receber R${aumento:.2f}')

'''salario = float(input('Qual o salário do funcionário: R$'))
aumento = salario + (salario * 15 / 100)
aumento2 = salario + (salario * 10 / 100)
if salario >= 1250.0:
    print('Um funcionário que ganhava R${:.2f}, com 10% de aumento passa a receber R${:.2f}'.format(salario, aumento2))
else:
    print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}'.format(salario, aumento))'''
