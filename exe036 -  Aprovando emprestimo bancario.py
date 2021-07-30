print("\033[1;30;107m""-=-""\033[m"""*15)
print("   EMPRESTIMO BANCÁRIO PARA SUA CASA NOVA")
print("\033[1;30;107m""-=-""\033[m"""*15)
casa = float(input("Qual o valor da casa que irá comprar R$:"))
salario = float(input("Qual o valor do seu salário R$"))
anos = int(input("E em quantos anos irá financiar?"))
prestacao = casa / (anos*12)
minima = salario * 30 / 100
print(f"Para pagar uma casa de R$ {casa:.2f} em {anos} anos,", end="")
print("a prestação será de R${:.2f}".format(prestacao))
if prestacao <= minima:
    print("EMPRESTIMO PODE SER CONCEDIDO..")
else:
    print("EMPRESTIMO NEGADO")

