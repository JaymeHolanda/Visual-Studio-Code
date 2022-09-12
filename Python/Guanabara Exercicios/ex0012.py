
# FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O PRODUTO COM 5% DE DESCONTO. 

produto = float(input(' Qual o preço do produto cadastrado   ') ) 
desconto = produto * 0.05
total = produto - desconto

print(f'Produto com o valor total de: R$ {produto}. Com o desconto de 5% de R$ {desconto:.2f}, \n logo o valor total é de R$ {total:.2f}.')