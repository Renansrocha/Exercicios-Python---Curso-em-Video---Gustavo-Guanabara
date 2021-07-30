print('{:^40}'.format('===============\033[4;34;33mLOJAS S.ROCHA\033[m================'))
preço = float(input("Qual valor das compras ? R$"))
print('''FORMA DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x cartão''')
opção = int(input("Qual opção? "))
dinheiro = preço - (preço*10/100)
cartaoavista = preço - (preço*5/100)
cartao2x = preço/2
if opção == 1:
    print("O valor da sua compra à vista/cheque tem 10% de desconto!")
    print("Você ira pagar apenas R${:.2f}.".format(dinheiro))
elif opção == 2:
    print("O valor da sua compra à vista no cartão tem 5% desconto!")
    print("Você ira pagar apenas R${:.2f}.".format(cartaoavista))
elif opção == 3:
    print("O valor da sua compra parcelada em 2x \033[4mNÂO TEM\033[m desconto!")
    print("Você ira pagar apenas R${:.2f} em cada parcela.".format(cartao2x))
elif opção == 4:
    parcela = int(input("Em quantas vezes ira pagar? "))
    juros3xoumais = (preço + (preço * 20 / 100)) / parcela
    totalparcelado = (preço + (preço * 20 / 100))
    print("O valor da sua compra parcelada em {}x tem juros de 20% no valor total da compra".format(parcela))
    print("Você ira pagar apenas R${:.2f} em cada parcela. Total da compra é de {:.2f}.".format(juros3xoumais, totalparcelado))
else:
    total = 0
    print("Opção invalida de pagamento. Tente novamente.")

