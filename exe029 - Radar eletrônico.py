velocidade= float(input("Qual a velocidade atual do carro? "))
multa =(velocidade-80)*7
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia ! Dirija com segurança !")


