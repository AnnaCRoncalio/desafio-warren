from itertools import combinations_with_replacement 
from functools import reduce 
from operator import add 

vetor = [1,2,3,4] # alterar valor conforme o desejado
numero_escolhido = 20 # alterar valor conforme o desejado

length_combinacoes = 1
while True:
    # print("Testando array com", length_combinacoes, "combinações")
    combinacoes = list(combinations_with_replacement(vetor, length_combinacoes)) 
    
    for combinacao in combinacoes: 
        soma_combinacao = reduce(add, combinacao) 
            
        if soma_combinacao == numero_escolhido: 
            print("Número escolhido:", numero_escolhido, " | vetor:", combinacao)
            break
            
    if soma_combinacao == numero_escolhido:
        break 
    else: 
        length_combinacoes += 1
