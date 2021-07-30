larg= float(input("Digite a largura da parede: "))
alt= float(input("Digite a altura da parede: "))
area= larg*alt
tinta= area/2
print("Sua parede tem a dimensão de {}x{} e sua aréa é de {}m².".format(larg,alt,area))
print("Para pintar essa parede, voce precisará de {} de tinta.".format(tinta))
