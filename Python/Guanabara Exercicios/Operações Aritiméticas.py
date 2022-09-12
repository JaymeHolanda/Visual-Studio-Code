# Operações Aritimétricas 
# // -> Divisão inteira 
# % -> Restante da divisão
# Raíz quadrada : n**(1/2)
# Precedência: 
#1 ()
#2 **
#3 * , / , // , %
#4 + , - ( binárias. Anotar Post) 
# ^ (Centraliza) > (a direita) < (A esquerda) // {v:(carac_ opicional)<>^} 
# Quebrar a linha = (Contra barra n) --> \n

n1 = float (input('Digite um número ') )
n2 = float (input ('Digite outro número ') )
s = n1 + n2
n = n1-n2
d = n1/n2
m = n1*n2
r = n1*n2/(1/2)
di = n1//n2

print(f'a soma é {s:_^5}!',end=' ')
print(f'A sub é {n:_^5}')
print(f'A divisão é {d:.4f}')
print(f'A divisão interna é {di:.3f}')
print(f'A multiplicação é {m:.5f}')
print(f'A raiz quadrada é igual {r}')  

