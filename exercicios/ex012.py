valor = float(input('Informe o valor do produto para receber o desconto: '))
desc = valor-(5/100*valor)
print('O produto com 5% de desconto foi para R${0:.2f}.' .format(desc))
