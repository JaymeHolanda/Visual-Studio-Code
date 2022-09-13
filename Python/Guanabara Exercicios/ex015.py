# ESCREVA UM PROGRAMA QUE PERGUNTE A: KM, QUANTIDADE DE DIAS, QUE ELE FOI ALUGADO.
# CALCULE O DIA. CARRO R$60.00 P/D E R$ 0.15 POR KM RODADO. 

km = float(input('Qual a quantidade de KM rodados ?    '))
dias = float(input('Qual a quantidade de dias ?  '))

valordias = dias * 60
valorkm = km * 0.15 

print(f'O valor gasto com o carro foi:')
print(f'Valor de diaria:R$ {valordias}')
print(f'Valor de KM gastos:R$ {valorkm}')

print(f'Portanto o valor total gasto foi de:R$ {valorkm+valordias}')