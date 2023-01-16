salario = float(input('Digite o salário do funcionário: '))
nvSala = salario + (15/100*salario)
print('O funcionário recebeu um aumento de 15% em seu salário. \nAgora ele recebe R${0:.2f}.' .format(nvSala))
