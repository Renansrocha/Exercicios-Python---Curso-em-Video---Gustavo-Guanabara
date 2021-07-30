n= float(input('Quanto dinheiro voce tem na carteira?: R$'))
dollar= n/5.22
euro= n/6.38
print ('Com R${:.2f} você pode comprar US${:.2f} e {:.2f} Euros '.format(n,dollar,euro))

