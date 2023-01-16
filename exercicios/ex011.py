altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
quadrado = (altura * largura)*2
litro = quadrado / 2
print('Para pintar {0:.2f}m² será necessário {1:.2f}l de tinta.' .format(quadrado, litro))
