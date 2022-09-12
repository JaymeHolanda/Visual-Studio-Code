# FAÇA UM PROGRAMA QUE MOSTRE O TYPE DO QUE FOI DIGITADOS E OS POSSÍVEIS TIPOS PRIMITIVOS
#DO QUE FOI DIGITADO.

n1 = (input ('Digite alguma coisa aqui...  ') )
print(f'O tipo primitivo desse valor é {type(n1)}') 
print('o que você digitou é um número ?', n1.isnumeric())
print('o que você digitou possui algum espaço ?', n1.isspace())
print('O que você digitou possui algum alfanumerico?',n1.isalnum())
print('O que você digitou é alfabético?', n1.isalpha())
print('O que você digitou possui algum caractere decimal ?', n1.isdecimal())
print('O que você digitou está com letras Maiúsculas?', n1.isupper())
print('O que você digitou está com letras Minusculas?', n1.islower())
print('O que você digitou está Capitalizada?', n1.istitle())

 # is.tittle = Capitaliada = Carro, Promogramador. 
 # não funciona com int e nem com float

