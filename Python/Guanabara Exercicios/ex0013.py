
# FAÇA UM ALGORITIMO QUE LEIA O SALÁRIO E MOSTRE A NOVA REMUNERAÇÃO COM ACRESCIMO DE 15%

salario = float(input('Salário atual do funcionário:   '))
acrescimo = salario * 0.15 
total = salario + acrescimo 

print(f'O salário atual do funcionário é de {salario:.2f}')
print(f'O acrescimo em reais do funcionário é de R$: {acrescimo:.2f}')
print(f'Logo o valor tota é de R$: {total:.2f}')

print(f'O tipo dessa variante é {type(salario)}')


