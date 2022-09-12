nome = (input('digite seu nome ..') )
idade = int(input('Digite sua idade aqui  '))

if  idade <= 15: 
    print(f'{nome} desculpe você não pode entrar nesta Festa! ')

elif idade <= 17:
    print(f' {nome} É Necessária documentação de emancipação.')
else:
    print(f'Pode entrar nessa festa {nome}') 