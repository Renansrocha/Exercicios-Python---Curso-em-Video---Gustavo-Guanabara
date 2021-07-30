#Simplificado
distancia = float(input("Qual a distância da sua viagem ? "))
print("Você está preste a começar uma viagem de {:.1f}Km.".format(distancia))
valor = distancia * 0.50 if distancia <= 200 else distancia*0.45
print("E o preço da sua viagem será de R${:.2f}".format(valor))

#Forma comum
'''distancia = float(input("Qual a distância da sua viagem ? "))
print("Você está preste a começar uma viagem de {:.1f}Km.".format(distancia))
valor1 = distancia*0.50
valor2 = distancia*0.45
if distancia <=200:
    print("E o preço da sua viagem será de R${:.2f}".format(valor1))
else:
    print("E o preço da sua viagem será de R${:.2f}".format(valor2))'''