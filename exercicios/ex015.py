dias=float(input('Quantos dias ficou com o carro? '))
kilom=float(input('Quantos kms percorreu nesses {0:.0f} dias?' .format(dias)))
pgkm=0.15*kilom
pgdias=60*dias
total=pgkm+pgdias
print('Você ficou {0:.0F} dias com o carro e percorreu {1:.2f}kms.\nPagamento por dias de uso: R${2:.2f}.\nPagamento por kms percorridos: R${3:.2f}.\nValor total a ser pago: R${4:.2F}.' .format(dias,kilom, pgdias, pgkm, total))
