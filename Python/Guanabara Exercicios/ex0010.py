
#FAÇA UM PROGRAMA QUE LEIA QUANTOS REAIS A PESSOA TEM E QUANTOS DOLARES A PESSOA PODE COMPRAR

# CONSIDERE 1 USD = 3,27

r = int (input ('Quanto você possui em reais na sua carteira ?  '))

d = r / 3.27  #USAR SEMPRE PONTO. E NÃO VIRGULA.

print(f'Com o seu valor atual em Reais de {r} R$. Irá conseguir comprar {d:.2f} USD!')
