print("\033[30;43m=-=\033[m"*10)
print(" BEM VINDO AO CALCULO DE IMC")
print("\033[30;43m=-=\033[m"*10)
peso = float(input("Qual seu peso?"))
alt = float(input("Qual sua altura?"))
imc = peso / (alt**2)
print("Seu IMC é: {:.1f}".format(imc))
if imc < 18.5:
    print("CUIDADO!!! Você está ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Parabéns voce está no PESO IDEAL")
elif 25 <= imc <30:
    print('CUIDADO!!! Você está SOBREPESO')
elif 30 <= imc < 40:
    print("CUIDADO!!! Você está com OBESIDADE")
elif imc >= 40:
    print("CUIDADO!!! Você está com OBESIDADE MÓRBIDA")

