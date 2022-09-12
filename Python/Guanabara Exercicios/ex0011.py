
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS. CALCULE SUA ÁREA
# E A QUANTIDADE DE TINTA QUE SERÁ NECESSÁRIA PARA PINTAR. 

#CADA LITRO DE TINTA GASTA 2M*2

l = float(input('Qual a largura da parade ?  ') )

a = float(input('Qual a altura da parede ?  '))

area = l * a  # A AREA JÁ ESTÁ CONVERTIDA PARA M * 2

tinta = 2

rendimento = area / tinta

print(f'Para pintar uma parede com {l} M de Largura e {a} Altura. \n Teriamos que comprar {rendimento} latas de tinta.')

